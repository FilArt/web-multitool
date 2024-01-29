from fastapi import FastAPI
from tortoise import Tortoise, connections, fields, models
from tortoise.log import logger

from .settings import Settings


class ShortenedLinks(models.Model):
    id = fields.IntField(pk=True, auto=True)
    original_url = fields.TextField()
    shortened_url = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    click_count = fields.IntField(default=0)

    def get_full_path(self):
        return f"/s/{self.shortened_url}"


async def init_db(app: FastAPI):
    settings = Settings()
    logger.info(
        "Tortoise-ORM started, %s, %s", connections._get_storage(), Tortoise.apps
    )
    await Tortoise.init(
        db_url=settings.db_url,
        modules={"models": ["core.models"]},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await connections.close_all()
    logger.info("Tortoise-ORM shutdown")
