def fibo(n):
    x1=0
    x2=1
    i=1
    while i<n:
        x3=x1+x2
        x1=x2
        x2=x3
        i=i+1
    return x3
x3=fibo(6)
print x3





