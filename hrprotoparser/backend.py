
from pathlib import Path
import traceback
from contextlib import contextmanager
from functools import wraps
from hl037utils.config import Config as C
import pkg_resources
import os

#from dbug import *

from traceback import print_exc

import time
import json

from .protocol_parser import Protocol

APP = 'hrprotoparser'

class Include(object):
  """
  Include function implementation tracking the include paths
  """
  def __init__(include_paths):
    self.include_paths = include_paths

  def __call__(self):
    raise NotImplementedError()
    

class Backend(object):
  def __init__(self, config):
    self.config = config


  @staticmethod
  def createConfig(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), 'wb') as f :
      f.write(pkg_resources.resource_string(APP, 'default/conf.py'))

  def installDefaultTemplates(self):
    from distutils.dir_util import copy_tree
    self.config.template_dir.mkdir(parents=True, exist_ok=True)
    pkg_resources.set_extraction_path(self.config.template_dir)
    dest = str(self.config.template_dir/'default/templates/') + '/'
    src = pkg_resources.resource_filename(APP, 'default/templates/')
    if src != dest :
      copy_tree(src, dest)
    return dest

  def installTemplate(self, name, src):
    from distutils.dir_util import copy_tree
    dest = self.config.template_dir / 'templates' / name
    copy_tree(str(src), str(dest))
    return dest
  
  def uninstallTemplate(self, name):
    from distutils.dir_util import remove_tree
    dest = self.config.template_dir / 'templates' / name
    remove_tree(str(dest))
    return dest

  def parseProtocol(self, f, filename):
    p = Protocol()
    p.parse(f, filename)
    return p

  def parsePlugin(self, path):
    from hl037utils.config import Config as C
    from tempiny import Tempiny
    tempiny = None
    plugin = None

    if path.is_file() :
      # source plugin.py if one
      with path.open('r') as f :
        obj = compile(f.read(), plugin, 'exec')
      g = C( args = args )
      exec(obj, {}, g)
      if 'conf' in g :
        conf = g.conf
        if 'tempiny' in conf :
          tempiny = [ (pattern, Tempiny(**c)) for pattern, c in conf.tempiny ]
      if 'plugin' in g :
        plugin = g.plugin
    if tempiny is None :
      tempiny = [ '*', Tempiny() ]
    return tempiny, plugin
    
  
  def findTemplate(self, template):
    """
    Find `template`. If `template` starts with a '@', then search in globally installed template.
    Else, if the path exists and point to a directoryn, return this directory.

    @return Path object to template root
    """
    if template[0] == '@' :
      p = self.config.template_dir/template[1:]
    else:
      p = Path(template)
    if not p.is_dir() :
      raise FileNotFoundError(p)
    return p
  
  def execTemplate(self, template_path : Path, dest : Path, args):
    from hl037utils.config import Config as C
    tempiny, plugin = self.parsePlugin(template_path / '__plugin.py')
    
    d = template_path / 'root'
    stack = [(False, d)]
    include_paths = []
    include = Include(include_paths)
    base_g = C(
      plugin=plugin,
      _p=plugin,
      include=include
    )
    while stack :
      
      seen, d = stack.pop()
      if seen :
        include_paths.pop()
        continue
      
      stack.push((True, d)
      include_paths.append(d/'__include')
      out = dest / d.relative_to(template_path)
      for p in d.iterdir() :
      
        if p.is_dir() :
          if p.name != '__include' :
            stack.push((False, p))
          continue
          
        out_name = p.name
        is_template = False
        is_opt = False
        if out_name.startswith('__opt_':
          is_opt = True
          out_name = out_name[len('__opt_'):]
        if out_name('__template_') :
          is_template = True
          out_name = out_name[len('__template_'):]
          
        if is_opt :
          if (out/out_name).exists() :
            continue
        if is_template :
          self.processFile(

          
          


    
        
      
    
      
    
  

  

    

