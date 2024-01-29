import pytest
from httpx import AsyncClient

from core.models import ShortenedLinks


@pytest.fixture
async def create_short_url(client: AsyncClient):
    async def _(original_url: str):
        response = await client.post("/shorten_url", json={"url": original_url})
        assert response.status_code == 200, response.text
        return response.json()

    yield _

    await ShortenedLinks.all().delete()


@pytest.mark.anyio
async def test_create_short_url(create_short_url):
    long_url = "https://test.com"
    generated_shortened_url = await create_short_url(long_url)
    generated_shortened_url = generated_shortened_url.replace("/s/", "")
    shortened_url = await ShortenedLinks.get(shortened_url=generated_shortened_url)
    assert shortened_url.original_url == long_url


@pytest.mark.anyio
async def test_get_short_url(client: AsyncClient, create_short_url):
    long_url = "https://test.com"
    short_url = await create_short_url(long_url)
    response = await client.get(short_url)
    assert response.status_code == 307
    assert response.next_request.url == long_url
