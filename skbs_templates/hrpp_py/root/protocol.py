## new_path = dest.with_name(_p.prefix + dest.name)
##
## from itertools import chain
##
## if int(_p.proto.F['FIXEDTSIZE'].val):
##    tsize = int(_p.proto.F['FIXEDTSIZE'].val)
## -
## else:
##    tsize = 0
## -
## if int(_p.proto.F['FIXEDSIZE'].val):
##    psize = int(_p.proto.F['FIXEDSIZE'].val)
## -
## elif _p.bool(_p.proto.F['VARSIZE'].val):
##    psize = 0
## -
## else:
##    psize = None
## -

from enum import Enum, IntEnum, auto
import struct
from typing import Type as _typehint_Type_

class FloatEnum(float, Enum):
  pass

{{include('constants.py')}}

{{include('structs.py', tsize=tsize, psize=psize)}}

{{include('parser.py', tsize=tsize, psize=psize)}}

