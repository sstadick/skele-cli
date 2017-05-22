"""
skele

Usage:
  skele hello
  skele -h | --help
  skele --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  skele hello

Help:
  <Link to documentation>
"""
import click
from . import __version__ as VERSION


@click.command()
def main():
    """Main CLI entrypoint."""
    pass
