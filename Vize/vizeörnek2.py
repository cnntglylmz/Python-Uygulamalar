pay=int(raw_input("Pay değerini girin:"))
payda=int(raw_input("Payda değerini girin:"))
if payda>pay:
    print "Basit kesir girdiniz."
elif payda==pay:
    print "Girdiğiniz deger bir tam sayıdır."
else:
    x=pay/payda
    y=pay%payda
    print "Bileşik bir kesir girdiniz. Kesrin değeri:",x,"tam",y,"/",payda,"dir."
