
import databases
import ormar
import sqlalchemy

DATABASE_URL = "sqlite:///db.sqlite"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# note that this step is optional -> all ormar cares is a internal
# class with name Meta and proper parameters, but this way you do not
# have to repeat the same parameters if you use only one database
class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class ShortURL(ormar.Model):
    class Meta(BaseMeta):
        tablename = "short_urls"

    value = ormar.Text(primary_key=True)


class LongURL(ormar.Model):
    class Meta(BaseMeta):
        tablename = "long_urls"

    value = ormar.Text(primary_key=True)
    short = ormar.ForeignKey(to=ShortURL)
