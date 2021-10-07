dizi=[15,16,15,14,16,15,15,14]
def soru1(dizi):
    toplam=0
    i=0
    while i<len(dizi):
        veri=dizi[i]
        basamak=1
        while veri>1:
            veri=veri/2
            basamak=basamak+1
        toplam=toplam+basamak
        i=i+1
    return toplam
toplam=soru1(dizi)
print toplam

def donus (dizi):
    yenidizi=[]
    yenidizi.append(dizi[0])
    i=0
    while i<len(dizi)-1:
        yenidizi.append(dizi[i+1]-dizi[i])
        i=i+1
    return yenidizi
son=donus(dizi)
print son
sonuc=soru1(son)
print sonuc
