n=10
x=list()
for i in range(n):
    y=list()
    for j in range(n):
        y.append(1) if (i+j)==n-1 or (i==j) else y.append(0)
    x.append(y)

for i in x:
    print i
