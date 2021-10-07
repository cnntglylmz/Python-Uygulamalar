sinif=[[123,'ahmet gel',10],[234,'mehmet git',75],[345,'bahri dur',67],
   [567,'burcu koþ',83],[678,'berna yaz',56],[789,'binan yak',78]]

def ogrencibul (sinif):
    eb=0
    for i in range (len(sinif)):
        if sinif[i][2]>eb:
            eb=sinif[i][2]
            isim=sinif[i][1]
    return isim
isim=ogrencibul(sinif)
print isim
