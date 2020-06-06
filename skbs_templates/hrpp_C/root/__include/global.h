
typedef void (*{{_p.prefix}}hrp_handler_t) ({{_p.prefix}}hrp_packet_t*);

typedef struct {{_p.prefix}}hrp_vector_s {
//# for p in _p.proto.P:
//#   sname = _p.struct_name(p)
  {{sname}}_handler_t {{sname}};
//# -
} {{_p.prefix}}hrp_vector_t;

typedef enum {{_p.prefix}}hrp_server_state_e {
//# if psize is not None:
  {{_p.prefix}}hrp_READ_SIZE,
  {{_p.prefix}}hrp_SKIP,
//# -
  {{_p.prefix}}hrp_READ_TYPE,
  {{_p.prefix}}hrp_READ,
} {{_p.prefix}}hrp_server_state_t;

typedef struct {{_p.prefix}}hrp_s {
  {{_p.prefix}}hrp_vector_t handler;
  {{_p.prefix}}hrp_server_state_t state;
  size_t remain;
  {{_p.prefix}}hrp_packet_t * current_packet; 
  unsigned char * current_ptr;
//# if psize is not None:
  {{_p.prefix}}hrp_stype_t n_h_read;
  {{_p.prefix}}hrp_stype_t size;
//# -
  {{_p.prefix}}hrp_ptype_t type;
} {{_p.prefix}}hrp_t;


#ifdef __cplusplus
extern "C" {
#endif
  
size_t {{_p.prefix}}hrp_packet_size({{_p.prefix}}hrp_ptype_t);

void {{_p.prefix}}hrp_server_handle_packet({{_p.prefix}}hrp_t * _this);

void {{_p.prefix}}hrp_server_parse({{_p.prefix}}hrp_t * _this, const void * data, size_t size);

void {{_p.prefix}}hrp_server_init({{_p.prefix}}hrp_t * _this);

//# if psize is None:
{{_p.prefix}}hrp_packet_t * {{_p.prefix}}hrp_palloc({{_p.prefix}}hrp_ptype_t); // user
//# -
//# else:
{{_p.prefix}}hrp_packet_t * {{_p.prefix}}hrp_palloc({{_p.prefix}}hrp_ptype_t, {{_p.prefix}}hrp_stype_t); // user
//# -

void {{_p.prefix}}hrp_pfree({{_p.prefix}}hrp_packet_t *); // user

#ifdef __cplusplus
}
#endif

