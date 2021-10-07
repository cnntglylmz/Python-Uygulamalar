kontrol=True
while kontrol:
    x=int (raw_input("Lütfen 1 ile 365 arasında bir sayı giriniz:"))
    if x>1 and x<=365:
        kontrol=False
    else:
        print "Lütfen koşullara uygun bir giriş yapınız."
kalan=x%7
if kalan==0:
    y="Cumartesi"
elif kalan==1:
    y="Pazar"
elif kalan==2:
    y="Pazartesi"
elif kalan==3:
    y="Salı"
elif kalan==4:
    y="Çarşamba"
elif kalan==5:
    y="Perşembe"
else:
    y="Cuma"
print "Bügün Cumartesi",x,"gün sonra haftanın",y,"günüdür."
