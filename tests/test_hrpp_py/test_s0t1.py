import pytest



@pytest.fixture(scope='module')
def parser_test_data(protocol):
  from itertools import count
  _p = protocol
  a = count(0, 5)
  return [
    (
      _p.packets.all_nums,
      (
        42,
        420,
        2**(24)+42,
        2**(48)+42,
        
        -42,
        -420,
        -2**(24)+42,
        -2**(48)+42,
        
        150,
        2**(16) - 42,
        2**(32) - 42,
        2**(64) - 42,
        
        42.41999816894531,
        42.41999816894531,
      ),
      lambda p2 : (
        p2.data.i8p,
        p2.data.i16p,
        p2.data.i32p,
        p2.data.i64p,
        p2.data.i8n,
        p2.data.i16n,
        p2.data.i32n,
        p2.data.i64n,
        p2.data.ui8p,
        p2.data.ui16p,
        p2.data.ui32p,
        p2.data.ui64p,
        p2.data.f32,
        p2.data.f64,
      ),
    ),
    
    (
      _p.packets.all_arrays,
      (
        [ 42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 420 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 2**(24)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 2**(48)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
            
        [ -42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ -420 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ -2**(24)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ -2**(48)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
            
        [ 130 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 2**(16) - 142 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 2**(32) - 142 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 2**(64) - 142 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
            
        [ 42.41999816894531 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        [ 42.41999816894531 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
      ),
      lambda p2 : (
        [ p2.data.i8p[i] for i in range(_p.array_size) ],
        [ p2.data.i16p[i] for i in range(_p.array_size) ],
        [ p2.data.i32p[i] for i in range(_p.array_size) ],
        [ p2.data.i64p[i] for i in range(_p.array_size) ],
        [ p2.data.i8n[i] for i in range(_p.array_size) ],
        [ p2.data.i16n[i] for i in range(_p.array_size) ],
        [ p2.data.i32n[i] for i in range(_p.array_size) ],
        [ p2.data.i64n[i] for i in range(_p.array_size) ],
        [ p2.data.ui8p[i] for i in range(_p.array_size) ],
        [ p2.data.ui16p[i] for i in range(_p.array_size) ],
        [ p2.data.ui32p[i] for i in range(_p.array_size) ],
        [ p2.data.ui64p[i] for i in range(_p.array_size) ],
        [ p2.data.f32[i] for i in range(_p.array_size) ],
        [ p2.data.f64[i] for i in range(_p.array_size) ],
      ),
    ),
    
    (
      _p.packets.array_struct_struct,
      (
        list(range(_p.array_size)),
        [ (1 + i, 2.5 + i, 3000 + i, 48.4568 + i) for i in range(_p.array_size) ],
        [ (2.5 + i, 48.4568 + i, 3000 + i, 1 + i) for i in range(_p.array_size) ],
        [ ((1 + i, 2.5 + i, 3000 + i, 48.4568 + i), (2.5 + i, 48.4568 + i, 3000 + i, 1 + i)) for _i in range(_p.array_size) for i in [_i + 100] ],
      ),
      lambda p2 : (
        [ p2.data.i8[i] for i in range(_p.array_size) ],
        [
          (
            p2.data.s1_[i].i8,
            p2.data.s1_[i].f,
            p2.data.s1_[i].i16,
            p2.data.s1_[i].d,
          )
          for i in range(_p.array_size)
        ],
        [
          (
            p2.data.s2_[i].f,
            p2.data.s2_[i].d,
            p2.data.s2_[i].i16,
            p2.data.s2_[i].i8,
          )
          for i in range(_p.array_size)
        ],
        [
          (
            (
              p2.data.s3_[i].s1_.i8,
              p2.data.s3_[i].s1_.f,
              p2.data.s3_[i].s1_.i16,
              p2.data.s3_[i].s1_.d,
            ),
            (
              p2.data.s3_[i].s2_.f,
              p2.data.s3_[i].s2_.d,
              p2.data.s3_[i].s2_.i16,
              p2.data.s3_[i].s2_.i8,
            ),
          )
          for i in range(_p.array_size)
        ],
      ),
    )
  ]


@pytest.fixture(scope='module')
def vl_in(protocol):
  from itertools import count
  _p = protocol
  a = count(0, 5)
  return [
    (
      _p.packets.varlen_val,
      (
        42,
        [ 523 * ( (-1) ** i ) for i in range(10) ],
      ),
      lambda p : (
        p.data.i8,
        [ p.data.vl_i16[i] for i in range(10) ]
      ),
    ),
    (
      _p.packets.varlen_val,
      (
        42,
        [],
      ),
      lambda p : (
        p.data.i8,
        [],
      ),
    ),
    (
      _p.packets.varlen_val,
      (
        42,
        [4242],
      ),
      lambda p : (
        p.data.i8,
        [p.data.vl_i16[0]],
      ),
    ),
    (
      _p.packets.varlen_struct,
      (
        list(range(_p.array_size)),
        [ (1 + i, 2.5 + i, 3000 + i, 48.4568 + i) for i in range(_p.array_size) ],
        (
          42,
          [ i + 20 for i in range(_p.array_size) ],
          [
            (
              [ (2.5 + i, 48.4568 + i, 3000 + i, 1 + i) for i in range(2) ],
              4242,
              (1 + 6 + j, 2.5 + 6 + j, 3000 + 6 + j, 48.4568 + 6 + j)
            )
            for j in range(10)
          ],
        ),
      ),
      lambda p : (
        [ p.data.i8[i] for i in range(_p.array_size) ],
        [
          (
            p.data.s1_[i].i8,
            p.data.s1_[i].f,
            p.data.s1_[i].i16,
            p.data.s1_[i].d,
          )
          for i in range(_p.array_size)
        ],
        (
          p.data.s5_.i8,
          [ p.data.s5_.ai8[i] for i in range(_p.array_size) ],
          [
            (
              [
                (
                  p.data.s5_.s4_vl[i].s2_[j].f,
                  p.data.s5_.s4_vl[i].s2_[j].d,
                  p.data.s5_.s4_vl[i].s2_[j].i16,
                  p.data.s5_.s4_vl[i].s2_[j].i8,
                )
                for j in (0,1)
              ],
              p.data.s5_.s4_vl[i].i16,
              (
                p.data.s5_.s4_vl[i].s1_.i8,
                p.data.s5_.s4_vl[i].s1_.f,
                p.data.s5_.s4_vl[i].s1_.i16,
                p.data.s5_.s4_vl[i].s1_.d,
              ),
            )
            for i in range(10)
          ]
        )
      )
    ),
    (
      _p.packets.varlen_struct,
      (
        list(range(_p.array_size)),
        [ (1 + i, 2.5 + i, 3000 + i, 48.4568 + i) for i in range(_p.array_size) ],
        (
          42,
          [ i + 20 for i in range(_p.array_size) ],
          [ ],
        ),
      ),
      lambda p : (
        [ p.data.i8[i] for i in range(_p.array_size) ],
        [
          (
            p.data.s1_[i].i8,
            p.data.s1_[i].f,
            p.data.s1_[i].i16,
            p.data.s1_[i].d,
          )
          for i in range(_p.array_size)
        ],
        (
          p.data.s5_.i8,
          [ p.data.s5_.ai8[i] for i in range(_p.array_size) ],
          [ ]
        )
      )
    ),
  ]


def test_generated(protocol):
  assert protocol is not None



def test_attr_access1(protocol):
  _p = protocol
  vals = (1, 2.5, 3000, 48.4568)
  s1 = _p.s1(vals)
  assert vals == (s1.i8, s1.f, s1.i16, s1.d)
  
def test_attr_access2(protocol):
  _p = protocol
  vals = ((1, 2.5, 3000, 48.4568), (2.5, 48.4568, 3000, 1))
  s3 = _p.s3(vals)
  assert vals == ((s3.s1_.i8, s3.s1_.f, s3.s1_.i16, s3.s1_.d), (s3.s2_.f, s3.s2_.d, s3.s2_.i16, s3.s2_.i8))

def test_attr_access3(protocol):
  _p = protocol
  vals = (
    list(range(_p.array_size)),
    [ (1 + i, 2.5 + i, 3000 + i, 48.4568 + i) for i in range(_p.array_size) ],
    [ (2.5 + i, 48.4568 + i, 3000 + i, 1 + i) for i in range(_p.array_size) ],
    [ ((1 + i, 2.5 + i, 3000 + i, 48.4568 + i), (2.5 + i, 48.4568 + i, 3000 + i, 1 + i)) for _i in range(_p.array_size) for i in [_i + 100] ],
  )
  p = _p.packets.array_struct_struct(vals)
  assert 48.4568 + 2 == p.data.s1_[2].d
  assert 3000 + 4 + 100 == p.data.s3_[-1].s1_.i16
  assert 3 == p.data.i8[3]

@pytest.mark.parametrize("i", range(5))
def test_attr_access_vl(protocol, vl_in, i):
  P, vals, f = vl_in[i]
  p = P(vals)
  assert vals == f(p)
  
  
def test_encode_decode1(protocol):
  _p = protocol
  vals = (
    42,
    420,
    2**(24)+42,
    2**(48)+42,
    
    -42,
    -420,
    -2**(24)+42,
    -2**(48)+42,
    
    150,
    2**(16) - 42,
    2**(32) - 42,
    2**(64) - 42,
    
    42.41999816894531,
    42.41999816894531,
  )
  p = _p.packets.all_nums(vals)
  b = p.encode()
  p2 = _p.packets.all_nums()
  p2.decode(b)
  
  assert vals == (
    p2.data.i8p,
    p2.data.i16p,
    p2.data.i32p,
    p2.data.i64p,
    p2.data.i8n,
    p2.data.i16n,
    p2.data.i32n,
    p2.data.i64n,
    p2.data.ui8p,
    p2.data.ui16p,
    p2.data.ui32p,
    p2.data.ui64p,
    p2.data.f32,
    p2.data.f64,
  )
  
  
def test_encode_decode2(protocol):
  from itertools import count
  _p = protocol
  a = count(0, 5)
  vals = (
    [ 42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 420 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 2**(24)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 2**(48)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        
    [ -42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ -420 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ -2**(24)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ -2**(48)+42 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        
    [ 130 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 2**(16) - 142 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 2**(32) - 142 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 2**(64) - 142 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
        
    [ 42.41999816894531 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
    [ 42.41999816894531 + i for a in [next(a)] for _i in range(_p.array_size) for i in [_i + a] ],
  )
  p = _p.packets.all_arrays(vals)
  b = p.encode()
  p2 = _p.packets.all_arrays()
  p2.decode(b)
  
  assert vals == (
    [ p2.data.i8p[i] for i in range(_p.array_size) ],
    [ p2.data.i16p[i] for i in range(_p.array_size) ],
    [ p2.data.i32p[i] for i in range(_p.array_size) ],
    [ p2.data.i64p[i] for i in range(_p.array_size) ],
    [ p2.data.i8n[i] for i in range(_p.array_size) ],
    [ p2.data.i16n[i] for i in range(_p.array_size) ],
    [ p2.data.i32n[i] for i in range(_p.array_size) ],
    [ p2.data.i64n[i] for i in range(_p.array_size) ],
    [ p2.data.ui8p[i] for i in range(_p.array_size) ],
    [ p2.data.ui16p[i] for i in range(_p.array_size) ],
    [ p2.data.ui32p[i] for i in range(_p.array_size) ],
    [ p2.data.ui64p[i] for i in range(_p.array_size) ],
    [ p2.data.f32[i] for i in range(_p.array_size) ],
    [ p2.data.f64[i] for i in range(_p.array_size) ],
  )
  
def test_encode_decode3(protocol):
  _p = protocol
  vals = (
    list(range(_p.array_size)),
    [ (1 + i, 2.5 + i, 3000 + i, 48.4568 + i) for i in range(_p.array_size) ],
    [ (2.5 + i, 48.4568 + i, 3000 + i, 1 + i) for i in range(_p.array_size) ],
    [ ((1 + i, 2.5 + i, 3000 + i, 48.4568 + i), (2.5 + i, 48.4568 + i, 3000 + i, 1 + i)) for _i in range(_p.array_size) for i in [_i + 100] ],
  )
  p = _p.packets.array_struct_struct(vals)
  b = p.encode()
  p2 = _p.packets.array_struct_struct()
  p2.decode(b)
  assert 48.4568 + 2 == p2.data.s1_[2].d
  assert 3000 + 4 + 100 == p2.data.s3_[-1].s1_.i16
  assert 3 == p2.data.i8[3]
  
  
@pytest.mark.parametrize("i", range(5))
def test_encode_decode_vl(protocol, vl_in, i):
  P, vals, f = vl_in[i]
  p = P(vals)
  b = p.encode()
  p2 = P()
  p2.decode(b)
  assert vals == f(p2)
  
def test_parser_1(protocol, Parser, parser_test_data):
  parser = Parser()
  P, vals, f = parser_test_data[0]
  b = P(vals).encode()
  parser.parse(b)
  assert 1 == len(parser.p_list)
  p = parser.p_list[0]
  assert isinstance(p, P)
  assert vals == f(p)

def test_parser_2(protocol, Parser, parser_test_data):
  parser = Parser()
  P, vals, f = parser_test_data[1]
  b = P(vals).encode()
  parser.parse(b)
  assert 1 == len(parser.p_list)
  p = parser.p_list[0]
  assert isinstance(p, P)
  assert vals == f(p)
  
def test_parser_3(protocol, Parser, parser_test_data):
  parser = Parser()
  P, vals, f = parser_test_data[2]
  b = P(vals).encode()
  parser.parse(b)
  assert 1 == len(parser.p_list)
  p = parser.p_list[0]
  assert isinstance(p, P)
  assert vals == f(p)

@pytest.mark.parametrize("i", range(5))
def test_encode_decode_vl(protocol, Parser, vl_in, i):
  parser = Parser()
  P, vals, f = vl_in[i]
  b = P(vals).encode()
  parser.parse(b)
  assert 1 == len(parser.p_list)
  p = parser.p_list[0]
  assert isinstance(p, P)
  assert vals == f(p)

