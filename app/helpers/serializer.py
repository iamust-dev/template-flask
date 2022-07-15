from marshmallow import Schema, fields

def unavatar(name):
  return f'https://unavatar.io/{name}'

class UserSchema(Schema):
  avatar = fields.Function(lambda user: unavatar(user.name))

  class Meta:
    fields = ('name', 'email', 'avatar', 'created_at', 'updated_at')

class PostSchema(Schema):
  user = fields.Nested(UserSchema)

  class Meta:
    fields = ('title', 'slug', 'body', 'user', 'created_at', 'updated_at')
