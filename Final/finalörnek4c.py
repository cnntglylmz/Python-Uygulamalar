sinif=[[123,'ahmet gel',10],[234,'mehmet git',75],[345,'bahri dur',67],
   [567,'burcu koþ',83],[678,'berna yaz',56],[789,'binan yak',78]]
def bilebas(sinif):
    ek=100
    for i in range (len(sinif)):
        isim=sinif[i][1]
        if isim [0]=='b':
            if sinif[i][2]<ek:
                ek=sinif[i][2]
                endusuk=sinif[i][0]
    return endusuk
en=bilebas(sinif)
print en
