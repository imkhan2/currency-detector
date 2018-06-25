n=int(input())
x=2
y=3
for i in range(1,n+1):
    for j in range(3-i):
        print(' ',end='')
    for j in range(i):
        z=x*y
        x=x+2
        y=y+4
        t=str(z)
        for k in range(5-len(t)):
            t='0'+t
        print(t,end=' ')
    print()