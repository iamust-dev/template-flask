from flask import Flask
from config.database import database

def create_app():
  app = Flask(__name__)

  @app.before_request
  def before_request():
    database.connect()

  @app.after_request
  def after_request(response):
    database.close()
    return response

  return app
