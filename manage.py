from config.application import create_app
from app.controllers import posts_controller
from lib.tasks.database import database_cli
from lib.tasks.graphql import graphql_cli

app = create_app()
app.cli.add_command(graphql_cli)
app.cli.add_command(database_cli)
app.add_url_rule('/posts', view_func=posts_controller.index)
app.add_url_rule('/posts/<int:post_id>', view_func=posts_controller.show)

if __name__ == '__main__':
  app.run()
