n=7
c=0
while 1:
    if n%7==0 and n%60==1:
        print(n)
        c=c+1
        if c==2:
            break
    n=n+1