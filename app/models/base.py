from peewee import Model
from config.database import database

class BaseModel(Model):
  class Meta:
    database = database
