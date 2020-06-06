"""
hrpotoparser C plugin.
"""

try:
  inside_skbs_plugin
except:
  from skbs.pluginutils import IsNotAModuleOrScriptError
  raise IsNotAModuleOrScriptError

conf = C(
  #   Predefined template syntax are Tempiny.PY, Tempiny.C and Tempiny.TEX :
  #   Tempiny.C  = dict(stmt_line_start=r'//#', begin_expr='{{', end_expr='}})
  #   Tempiny.PY = dict(stmt_line_start=r'##', begin_expr='{{', end_expr='}}')
  #   Tempiny.TEX = dict(stmt_line_start=r'%#', begin_expr='<<', end_expr='>>')
  # tempiny = [
  #   ('*' : Tempiny.PY)
  # ],
  opt_prefix = '_opt.',
  force_prefix = '_force.',
  raw_prefix = '_raw.',
  template_prefix = '_template.',
  #   pathmod_filename = '__pathmod',
)
conf.dir_template_filename = conf.template_prefix

from hrprotoparser.cli import hrprotoparser_cmd

plugin = C()
p = plugin

# Put above additionnal options / arguments
@hrprotoparser_cmd()
def hrpp_cli(**kwargs):
  """
  hrpotoparser C plugin.
  """
  plugin.update(kwargs)




invokeCmd(hrpp_cli, args)

def export(f):
  plugin[f.__name__] = f
  return f

c_types = {
    'int8'  : ('int8_t', 1),
    'char'  : ('char', 1),
    'uint8' : ('uint8_t', 1),
    'byte'  : ('unsigned char', 1),
    'int16' : ('int16_t', 2),
    'uint16': ('uint16_t', 2),
    'int32' : ('int32_t', 4),
    'uint32': ('uint32_t', 4),
    'int64' : ('int64_t', 8),
    'uint64': ('uint64_t', 8),
    'float' : ('float', 4),
    'double': ('double', 8),
    'usize' : ('size_t', None),
    'size'  : ('ssize_t', None),
}
plugin.c_types = c_types

@export
def cName(s):
  n = s.name
  r = n[0].lower()
  for c in n[1:]:
    if c.isupper():
      r += '_'+c.lower()
    else:
      r += c
  return 'ft_' + r


@export
def struct_name(s):
  if s.order is 2:
    return "ft_{}".format(s.name)
  else:
    return "ft_p_{}".format(s.name)
  
@export
def getCType(f):
  t = f.type
  a = ''
  flexible = False;
  while t.order is _P.Array.order:
    if t.nb is None:
      flexible = True
      a += ')'
    else:
      a = a + '[{}]'.format('FT_' + t.nb.name if t.nb.kind is protocol_parser.Constant.NAMED else str(t.nb.computed))
    t = t.t
  if t.order is 0:
    tt = c_types[t.name][0]
  elif t.order is 2 or t.order is 3:
    tt = struct_name(t) + "_t"
  elif t.order is 4:
    tt = cName(t) + "_t"
  else:
    tt = t.name
  if flexible :
    tt = 'FLEXIBLE_ARRAY('+tt+','
  return tt, a


@export
def comment(f):
  if f.comment is None:
    return ''
  else:
    return '// ' + f.comment

@export
def addStruct(s):
  exec(struct_code)

@export
def structArg(f):
  t = f.type
  if t.order is 4:
    t = t.type
  if t.order is 0:
    return f.name
  if t.order is 1:
    if t.t.name =='char':
      return f.name
  return '*'+f.name

@export
def sizeof2(t):
  if t.order is 0:
    return (c_types[t.name][1], True)
  if t.order is 1:
    if t.nb is None:
      return (0, False)
    size, constlen = sizeof2(t.t)
    if not constlen:
      raise RuntimeError('Array of varlen Struct')
    return (t.nb.computed * size, True)
  if t.order is 2 or t.order is 3:
    s = [size if cl else False for size, cl in (sizeof2(f.type) for f in t.fields)]
    #print(s)
    if len(s) is 0:
      return (0, True)
    if False in s[:-1]:
      raise RuntimeError('Struct with varlen field not at end')
    return (sum(s), s[-1] != False)
  if t.order is 4:
    return sizeof2(t.type)
  if t.order is 5:
    return sizeof2(t.alias)
  raise NotImplementedError('self.order == {} is not handled'.format(t.order))

@export
def sizeof(t):
  return sizeof2(t)[0]

@export
def lastRecType(s):
  d = 0
  f = s.fields[-1].name
  t = s.fields[-1].type
  while t.order is not 1:
    if t.order is 0 or t.order is 4:
      raise RuntimeError()
    if t.order is 5:
      t = t.alias
      continue
    else:
      d += 1
      t = t.fields[-1].type
  if t.nb is not None:
    raise RuntimeError()
  return (t.t, f + '[-1]' * d)

