n=int(input('>>> '))
sum=0
m=1
while n>=m:
    k=str(1)*m
    print(k,end=' ')
    if m<n:
        print('+',end=' ')
    else:
        print('=',end=' ')
    sum+=int(k)
    m+=1
print(sum)