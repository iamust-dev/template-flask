import os
from playhouse.db_url import connect
from config.environment import environment

def connect_database():
  return connect(os.environ.get('DATABASE_URL') or f'sqlite:///db/{environment}.sqlite')

database = connect_database()
