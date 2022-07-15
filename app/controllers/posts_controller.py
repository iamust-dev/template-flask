from flask import jsonify
from app.models import Post
from app.helpers.serializer import PostSchema

def index():
  posts = Post.select()
  return jsonify(PostSchema().dump(posts, many=True))

def show(post_id):
  post = Post.get(post_id)
  return jsonify(PostSchema().dump(post))
