sayi=int(raw_input("Pozitif bir say� giriniz:"))
s=0
for i in range(2,sayi+1):
    if sayi%i==0:
        s=s+1
if s==1:
    print "Asal say�d�r."
else:
    print "Asal say� de�ildir."
