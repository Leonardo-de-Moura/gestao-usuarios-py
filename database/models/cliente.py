from peewee import Model, CharField
from database.database import db


class Cliente(Model):
    name = CharField(default="sem nome")
    email = CharField()

    class Meta:
        database = db