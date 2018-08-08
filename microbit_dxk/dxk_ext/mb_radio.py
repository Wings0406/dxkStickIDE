import radio
from microbit import i2c
def channel():
  return i2c.read(0x20,1)[0]%32
def group():
  return i2c.read(0x20,1)[0]//32
def _send(bytes):
  radio.send_bytes(bytes)
  res,tmp=[],radio.receive_bytes()
  while tmp:
    res.append(tmp)
    tmp=radio.receive_bytes()
  return res
def send(id,bseq,size,to_int):
  radio.config(channel=i2c.read(0x20,1)[0]%32)
  res=radio.send_bytes(b'%s\r%s\r%s'%(id,size,bseq))
  res,tmp=[],radio.receive_bytes()
  if to_int:
    res=[int.from_bytes(t,'big') for t in res]
  return res
def r_eval(seq,grp=-1):
  gid=i2c.read(0x20,1)[0]
  radio.config(channel=gid%32)
  return _send(b'%s\r%s'%(gid,seq))