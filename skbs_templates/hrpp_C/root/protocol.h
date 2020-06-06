//# new_path = dest.with_name(_p.prefix + dest.name)

//# if _p.bool(_p.proto.F['FIXEDTSIZE'].val):
//#    tsize = int(_p.proto.F['FIXEDTSIZE'].val) * 8
//# -
//# else:
//#    tsize = 0
//# -

//# if _p.bool(_p.proto.F['FIXEDSIZE'].val):
//#    psize = int(_p.proto.F['FIXEDSIZE'].val) * 8
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
