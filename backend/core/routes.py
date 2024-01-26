from fastapi import APIRouter

router = APIRouter()


@router.post(path='/short-url')
async def create_short_url(long_url: str) -> str:
    pass