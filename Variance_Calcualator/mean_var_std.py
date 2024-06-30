import numpy as np
l=[]
def Calculate(lst):
    ar=np.array(lst)
    ar=ar.reshape((3,3))
    mean=[list(np.mean(ar,axis=0)),list(np.mean(ar,axis=1)),(np.mean(ar.flatten()))]
    variance=[list(np.var(ar,axis=0)),list(np.var(ar,axis=1)),(np.var(ar.flatten()))]
    st_dev=[list(np.std(ar,axis=0)),list(np.std(ar,axis=1)),(np.std(ar.flatten()))]
    max=[list(ar.max(axis=0)),list(ar.max(axis=1)),(np.max(ar.flatten()))]
    min=[list(ar.min(axis=0)),list(ar.min(axis=1)),(np.min(ar.flatten()))]
    sum=[list(ar.sum(axis=0)),list(ar.sum(axis=1)),(np.sum(ar.flatten()))]

    d={"Mean":mean,"Variance":variance,"Standard Deviation":st_dev,"Max":max,"Min":min,"Sum":sum}
    return d

for i in range(9):
   x=int(input("Enter a Number:"))
   l.append(x)
print(Calculate(l))
