bit=[15,16,15,14,16,15,15,14]
def bit_bul(sayi):
    sayac=0
    if sayi<=0:
        sayi=sayi*(-1)
        sayac=sayac+1
    while sayi>0:
        sayi=sayi/2
        sayac=sayac+1
    return sayac

def dizi_bit(a):
    toplam=0
    for i in range (len(a)):
        toplam=toplam+bit_bul(a[i])
    return toplam
sonuc=dizi_bit(bit)
print sonuc


def donus (a):
    b=[]
    b.append(a[0])
    for i in range (len(a)-1):
        b.append(a[i+1]-a[i])
    return b

son=donus(bit)
print son

sonuc2=dizi_bit(son)
print sonuc2

