from num import *
import numpy as np
u=[[1,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,1]]
q,d,e=tred2(u)
a,z=tqli(d,e,q)
print(np.array(a))
print(np.array(z))
