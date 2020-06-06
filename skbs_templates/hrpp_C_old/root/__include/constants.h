


#ifdef __cplusplus

##for e in E:
typedef enum {{cName(e)}}_e : {{c_types[e.type.name][0]}} {
## suffix = '' if not e.type or e.type.name[0] != 'u' else 'U'
## for f in e.constants:
   FT_{{f.name}} = {{f.computedStr}}{{suffix}}, {{comment(f)}}
## -
} {{cName(e)}}_t;

##-


##for c in G:
constexpr {{c_types[c.type][0]}} FT_{{c.name}} = {{c.computedStr}}{{'' if c.type[0] != 'u' else 'U'}};
##-

#else

##for e in E:
enum {{cName(e)}}_e{
## suffix = '' if not e.type or e.type.name[0] != 'u' else 'U'
## for f in e.constants:
   FT_{{f.name}} = {{f.computedStr}}{{suffix}}, {{comment(f)}}
## -
};
typedef {{c_types[e.type.name][0]}} {{cName(e)}}_t ;

##-

##signed = [c for c in G if c.type[0] != 'u']
##unsigned = [c for c in G if c.type[0] == 'u']

##if len(signed):
enum {
## for c in signed:
   FT_{{c.name}} = {{c.computedStr}},
## -
};
##-

##if len(unsigned):
enum {
## for c in unsigned:
   FT_{{c.name}} = {{c.computedStr}}U,
## -
};
##-

#endif


