import click
from flask.cli import AppGroup
from app.graphql import schema

graphql_cli = AppGroup('graphql')

@graphql_cli.command('execute')
@click.argument('query_string')
def execute_query(query_string):
  result = schema.execute(query_string)
  click.echo(result.data)
