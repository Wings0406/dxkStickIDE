from mb import _exe as C,gc
_=b'%c%c%c'
def setup(grps,addr):
	cmd=b'init%c'%len(grps)
	for t in grps:
		cmd+=b'%c'%t
	C(addr,cmd,1)
def set_pixel(g,pos,c,addr):
	C(addr,b'setP%c%c'%(g,pos)+_%c,1)
def set_pixel_range(g,pos,cs,addr):
	i,X=0,len(cs)
	while i<X:
		css=cs[i:i+8]
		cmd=b'setL'+_%(g,pos,len(css))
		for c in css:
			cmd+=_%c
		C(addr,cmd,1)
		i+=8;pos+=8
def set_xy(g,x,y,c,addr):
	C(addr,b'setX%c%c%c'%(g,x,y)+_%c,1)
def fill(g,c,addr):
	C(addr,b'fill%c'%g+_%c,1)
gc()