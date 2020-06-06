#ifndef PROTOCOL_H
#define PROTOCOL_H

#ifdef __cplusplus

#include <cinttypes>
#include <climits>
#include <cstdlib>


template <typename T>
class FlexibleArray
{
public:
   inline FlexibleArray(){}
   inline ~FlexibleArray(){}
   inline T & operator[](size_t ind){
      return reinterpret_cast<T*>(this)[ind];
   }
   inline operator T * () { return reinterpret_cast<T*>(this); }
};

#define FLEXIBLE_ARRAY(t, f) FlexibleArray<t> f

#else

#define FLEXIBLE_ARRAY(t, f) t f[0]

#if defined(__WINE__)

typedef __int8 int8_t;
typedef unsigned __int8 uint8_t;
typedef __int16 int16_t;
typedef unsigned __int16 uint16_t;
typedef __int32 int32_t;
typedef unsigned __int32 uint32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;

#else

#include <inttypes.h>
#include <limits.h>
#include <stdlib.h>

#endif

#endif

typedef enum ft_bp_e {
   FT_BP_HIST = 1,
   FT_BP_MAN,
   FT_BP_PROV,
   FT_BP_AGENT,
   FT_BP_05,
   FT_BP_06,
   FT_BP_07,
   FT_BP_08,
   FT_BP_09,
   FT_BP_10,
   FT_BP_11,
   FT_BP_12,
   FT_BP_EXPERT,
   FT_BP_GP,
   FT_BP_ANSWER,
   FT_BP_ERROR,
   FT_BP_NB,
} ft_bp_t;

