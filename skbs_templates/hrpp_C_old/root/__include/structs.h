

#pragma pack(push, 1)
##sname = struct_name(s)
##if s.order is protocol_parser.Struct.order:
typedef struct {{sname}}_s {
## for f in s.fields:
##    t, array = getCType(f)
   {{t}} {{f.name}}{{array}}; {{comment(f)}}
## -
#ifdef __cplusplus
   static constexpr size_t packet_size = {{sizeof(s)}};
#endif
} {{sname}}_t;
#ifdef __cplusplus
constexpr size_t sizeof_{{sname}} = {{sname}}_t::packet_size;
#else
static const size_t sizeof_{{sname}} = {{sizeof(s)}};
#endif
##-
##elif s.order is protocol_parser.Packet.order:
typedef struct {{sname}}_data_s {
## for f in s.fields:
##    t, array = getCType(f)
   {{t}} {{f.name}}{{array}}; {{comment(f)}}
## -
} {{sname}}_data_t;
typedef struct {{sname}}_s {
#ifdef __cplusplus
## if s.type is not None and s.type.name not in ('ANSWER', 'P_ANSWER', 'GENERIC', 'P_GENERIC', 'ERROR', 'P_ERROR'):
   static constexpr {{c_types[c.type][0]}} p_type = FT_{{s.type.name}};
## -
   static constexpr size_t packet_size = {{sizeof(s)}};
#endif
   ft_header_t header;
   union {
      {{sname}}_data_t data;
      FLEXIBLE_ARRAY(char, raw_data);
      FLEXIBLE_ARRAY(unsigned char, raw_data_uchar);
   };
} {{sname}}_t;
#ifdef __cplusplus
constexpr size_t sizeof_{{sname}} = {{sname}}_t::packet_size;
#else
static const size_t sizeof_{{sname}} = {{sizeof(s)}};
#endif
##-
##elif s.order is protocol_parser.Alias.order:
typedef {{struct_name(s.alias)}}_t {{sname}}_t;
#ifdef __cplusplus
constexpr size_t sizeof_{{sname}} = {{sname}}_t::packet_size;
#else
static const size_t sizeof_{{sname}} = {{sizeof(s)}};
#endif
##-
#pragma pack(pop)


