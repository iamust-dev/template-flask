from flask import Flask, abort
from peewee import DoesNotExist
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

  @app.errorhandler(DoesNotExist)
  def does_not_exist(e):
    return abort(404)

  return app
