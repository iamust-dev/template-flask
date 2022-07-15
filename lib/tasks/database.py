import click
import json
from flask.cli import AppGroup
from flask_bcrypt import Bcrypt
from app.models import Post, User
from app.models.base import database

bcrypt = Bcrypt()
database_cli = AppGroup('database')

def load_json(basename):
  with open(f'db/{basename}') as file:
    return json.load(file)

def build_user(name):
  email = f'{name}@users.noreply.github.com'
  digest = bcrypt.generate_password_hash(f'hash_{name}')
  return User.get_or_create(name=name, email=email, defaults={'password_digest': digest})

@database_cli.command('init')
def init_database():
  database.connect()
  database.create_tables([Post, User])

  User.truncate_table()
  Post.truncate_table()

  repos = load_json('repos.json')
  for repo in repos:
    user, created = build_user(repo['owner']['login'])
    Post.create(title=repo['name'], slug=repo['full_name'], body=repo['description'], user=user)

  database.close()
