import os
from typing import Final

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from core.main import app

DB_URL: Final[str] = "sqlite://:memory:"


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module")
async def client():
    os.environ["db_url"] = DB_URL
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c
