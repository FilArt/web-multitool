from .models import LongURL


class Shortener:
    async def generate_short_url(self, url: str) -> str:
        existing_url = await LongURL.objects.get_or_none(value=url)
        if existing_url:
            return existing_url
        
        ...
