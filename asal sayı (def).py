def asalmi(x=2):
    asal=True
    for i in range(2,(x/2)+1):
        if x%i==0:
            asal=False
            break
    return asal

x=107
if asalmi(x):
    print x,"Asal say�d�r."
else:
    print x,"Asal say� de�ildir."

print asalmi()   #parametresiz �a��r�l�nca x=2 default de�er ge�erli olur.
