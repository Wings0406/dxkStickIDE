from mb import *
def temp(addr=None):
  return command(slot(addr,2),b'get_temp',1)
def humi(addr=None):
  return command(slot(addr,2),b'get_humi',1)
def temp_humi(addr=None):
  res=command(slot(addr,2),b'get_temp_humi',2)
  return res//256,res%256