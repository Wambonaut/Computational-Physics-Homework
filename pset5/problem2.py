import numpy as np
from num import *
import matplotlib.pyplot as plt
all_EV=[]
all_anal=[]
diff=[]
for N in range(15, 31):
    Q1=[[np.sqrt(n+1)/np.sqrt(2) if n==m-1 else 0 for n in range(N)] for m in range(N)]
    Q2=[[np.sqrt(n)/np.sqrt(2) if n==m+1 else 0 for n in range(N)] for m in range(N)]
    Q=[[sum(x) for x in zip(row1,row2)] for row1, row2 in zip(Q1, Q2)]

    h0=np.identity(N)*np.array([n+0.5 for n in range(N)])
    Q=np.array(Q)
    Q4=Q.dot(Q).dot(Q).dot(Q)
    h=0.1*Q4+h0
    hl=[list(a) for a in h]

    q,d,e=tred2(hl)
    z,a=tqli(d,e,q)
    z=np.array(z)
    z.sort()

    anal=np.diag(h)
    anal=np.sort(anal)
    all_anal.append(anal)
    diff.append(max(np.abs(z-anal)))

    all_EV.append(z)
##print EV for Latex
print("\\\\\n".join(["&".join([str(np.round(i,3)) for i in j]) for j in all_anal]))
##just print EV
print(all_EV)

plt.plot(range(15,31),diff)
plt.xlabel("Dimension")
plt.ylabel("Eigenvalue Difference")
plt.savefig("fig1.pgf")
plt.show()
