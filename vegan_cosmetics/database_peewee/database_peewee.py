from peewee import *

db = SqliteDatabase('users.db')

class User(Model):
    name = CharField()
    password = CharField()
    class Meta:
        database = db # This model uses the "users.db" database.

class FileStorage(Model):
    owner = ForeignKeyField(User, backref='files')
    file_name = CharField()
    class Meta:
        database = db # this model uses the "users.db" database

db.connect()
db.create_tables([User,FileStorage])