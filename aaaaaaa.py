dizi=[15,16,15,14,16,15,15,14]
def ornek(dizi):
    toplam=0
    for i in range(len(dizi)):
        veri=dizi[7]
        basamak=1
        while veri>1:
            veri=veri/2
            basamak=basamak+1
        toplam=toplam+basamak
    return toplam
toplam=ornek(dizi)
print toplam
        
