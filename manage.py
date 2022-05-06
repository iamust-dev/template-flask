from config.application import create_app
from lib.tasks.database import database_cli
from lib.tasks.graphql import graphql_cli

app = create_app()
app.cli.add_command(graphql_cli)
app.cli.add_command(database_cli)

if __name__ == '__main__':
  app.run()
