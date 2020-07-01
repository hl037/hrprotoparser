import pytest
from tempfile import TemporaryDirectory
from pathlib import Path
from skbs.cli import main


@pytest.fixture(scope='module')
def protocol(request):
  proto = Path(request.fspath).with_suffix('') / 'protocol'
  #with TemporaryDirectory() as dest_s :
  dest_s = TemporaryDirectory()
  try:
    dest = Path(dest_s.name)
    main.main(['gen', '@hrpp_py', str(dest), '-g', '--', '-p', str(proto)], standalone_mode=False)
    import importlib.util
    spec = importlib.util.spec_from_file_location("protocol", str(dest/'protocol.py'))
    protocol = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(protocol)
  except :
    import pdb; pdb.xpm()
  yield protocol
  dest_s.cleanup
    

@pytest.fixture(scope='module')
def Parser(protocol):
  class Parser(protocol.Parser):
    def __init__(self, *args, **kwargs):
      self.p_list = []
      super().__init__(*args, **kwargs)

    def default_handler(self, p):
      self.p_list.append(p)

  return Parser
  

