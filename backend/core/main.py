import random
import string
from contextlib import asynccontextmanager

from fastapi import Body, FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse

from .models import ShortenedLinks, close_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(app)
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)


@app.post("/shorten_url")
async def create_short_url(url: str = Body(embed=True)):
    already_existing = await ShortenedLinks.get_or_none(original_url=url)
    if already_existing:
        return already_existing.shortened_url
    else:
        chars = string.ascii_letters + string.digits
        random_string = "".join([random.choice(chars) for _ in range(5)])
        sl = await ShortenedLinks.create(original_url=url, shortened_url=random_string)
        return sl.get_full_path()


@app.get("/s/{path}")
async def get_short_url(path: str):
    sl = await ShortenedLinks.get(shortened_url=path)
    if sl:
        original_url = sl.original_url
        return RedirectResponse(original_url)
    raise HTTPException(status_code=404)
