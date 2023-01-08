for i in range(100):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        i=int(str(i)[::-1])
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
            print(str(i)[::-1], end=' ')