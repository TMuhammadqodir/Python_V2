n=1
s=0
s1=1
while 1000>n:
    m=n
    k=2
    while m!=1:
        if m%k==0:
            s+=1
            m/=k
        else:
            s1*=(s+1)
            s=0
            k+=1
    else:
        s1*=(s+1)    
    if s1==9:
        print(n,end=' ')
    s=0
    s1=1
    n+=1
