kontrol=True
a=8
b=30
while kontrol:
    x=int(raw_input("100 ile 500 arasında bir sayı girin:"))
    if x>=100 and x<=500:
        kontrol=False
    else:
        print "Lütfen belirtilen koşullara uygun değer girin."
s=x/60
d=x%60
saat=s+a
dakika=b+d
if dakika>=60:
    saat=saat+1
    dakika=dakika%60
    if dakika==0:
        dakika=00
        print "Sınavın başlangıç saati 8:30'dur",x,"dakika sonra",saat,":",dakika,"olacaktır."

