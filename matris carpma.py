n=3
import random

def matris_olustur():
    x=[[random.randint(1,9) for c in range(n)] for i in range(n)]
    return x

def carp(a,b):
    for i in range(n):
        for j in range(n):
            t=0
            for k in range(n):
                t+=a[i][k]*b[k][j]
            c[i][j]=t
    return c

a=matris_olustur()
b=matris_olustur()
c=matris_olustur()

print a
print b
c=carp(a,b)
print c
