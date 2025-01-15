from peewee import Model, CharField
from database.data import db


class Cliente(Model):
    name = CharField(default="sem nome")
    email = CharField()

    class Meta:
        database = db