import click

from .commands.addchart import addchart 
from .commands.installchart import installchart
from .commands.artifactory import artifactory

@click.group()
def cli():

    """You can use this cli to add and install any helm chart you need\n
    and you can install the chart of the best Company JFROG :) by Typing helmcli artifactory"""
    pass


click.echo(click.style('Hello to the HelmCli', fg='green'))
cli.add_command(addchart)
cli.add_command(installchart)
cli.add_command(artifactory)


if __name__ == '__main__':
    cli()


