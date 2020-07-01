//# new_path = dest.with_name(_p.prefix + dest.name)
//#
//# from itertools import chain
//#
//# if int(_p.proto.F['FIXEDTSIZE'].val):
//#    tsize = int(_p.proto.F['FIXEDTSIZE'].val)
//# -
//# else:
//#    tsize = 0
//# -
//# if int(_p.proto.F['FIXEDSIZE'].val):
//#    psize = int(_p.proto.F['FIXEDSIZE'].val)
//# -
//# elif _p.bool(_p.proto.F['VARSIZE'].val):
//#    psize = 0
//# -
//# else:
//#    psize = None
//# -

{{include('header.h', tsize=tsize, psize=psize)}}
 
{{include('constants.h', tsize=tsize, psize=psize)}}

{{include('structs.h', tsize=tsize, psize=psize)}}

{{include('global.h', tsize=tsize, psize=psize)}}

{{include('footer.h', tsize=tsize, psize=psize)}}
