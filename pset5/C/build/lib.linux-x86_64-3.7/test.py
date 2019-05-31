from num import *
import numpy as np
u=[[1,0,1,1],[0,1,0,1],[1,0,1,0],[1,1,0,1]]
q,d,e=tred2(u)
a,z=tqli(d,e,q)
print("d",d,"e",e)
print("a",np.array(a))
print("z","\\\\\n".join(["&".join([str(np.round(i,3)) for i in j]) for j in z]))
