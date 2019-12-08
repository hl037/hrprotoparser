
import appdirs
import os
from hl037utils.config import Config as C

config_dir = appdirs.user_config_dir('hrprotoparser', 'Léo Flaventin Hauchecorne')

default_config = os.path.join(config_dir, 'conf.py')

def getConfig(path = None):
  if path is None :
    path = default_config
  with open(path, 'r') as f :
    obj = compile(f.read(), path, 'exec')
  conf = C()
  exec(obj, {}, conf)
  conf.config_path = path
  return conf

def getBackend(path = None):
  from hrprotoparser.backend import Backend as B
  return B(getConfig(path))


