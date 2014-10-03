import numpy as np
import os
ptg=np.array((0.1,1,2,5,7))
for k in ptg:
    pct=k*0.1
    ttl=
    N=int(pct*ttl)
    rng=np.arange(0,ttl+1)
    x=rng
    rng=np.delete(rng,ttl/2) 
    r_dir='  '
    os.system('mkdir '+r_dir)
    for t in range(100,500):
        a=np.random.permutation(rng)[:N]
        a=np.sort(a)
        rf=r_dir+'/'+'  '+str(int(k))+str(t)+'.txt'
        f = open(rf,'w')
        for i in range(0,len(a)):
            f.write(str(a[i]))
            f.write('\t')
        f.close()
