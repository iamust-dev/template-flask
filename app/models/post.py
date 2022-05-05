from app.models.base import BaseModel
from app.models.user import User
from datetime import datetime
from peewee import *

class Post(BaseModel):
  title = CharField(max_length=255)
  slug = CharField()
  body = TextField()
  published_at = DateTimeField(null=True)
  created_at = DateTimeField(default=datetime.now)
  updated_at = DateTimeField(default=datetime.now)
  user = ForeignKeyField(User, backref='posts')
