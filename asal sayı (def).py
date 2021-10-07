def asalmi(x=2):
    asal=True
    for i in range(2,(x/2)+1):
        if x%i==0:
            asal=False
            break
    return asal

x=107
if asalmi(x):
    print x,"Asal sayýdýr."
else:
    print x,"Asal sayý deðildir."

print asalmi()   #parametresiz çaðýrýlýnca x=2 default deðer geçerli olur.
