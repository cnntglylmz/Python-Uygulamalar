sayi=int(raw_input("Pozitif bir sayý giriniz:"))
s=0
for i in range(2,sayi+1):
    if sayi%i==0:
        s=s+1
if s==1:
    print "Asal sayýdýr."
else:
    print "Asal sayý deðildir."
