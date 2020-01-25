
import click
from functools import wraps
from .protocol_parser import Protocol

from pathlib import Path

def hrprotoparser_cmd(*args, **kwargs):
  def decorator(f):
    @click.option('--proto', '-p', type=click.Path(exists=True, dir_okay=False, readable=True), required=True)
    @click.command()
    def main(proto, **kwargs):
      p = Protocol(*args, **kwargs)
      with open(proto, 'r') as f :
        p.parse(f, proto)
      f(p, **kwargs)
    return main
  return decorator
    

