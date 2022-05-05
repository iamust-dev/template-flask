from app.models.base import BaseModel
from datetime import datetime
from peewee import *

class User(BaseModel):
  name = CharField()
  email = CharField(unique=True)
  password_digest = CharField()
  created_at = DateTimeField(default=datetime.now)
  updated_at = DateTimeField(default=datetime.now)
