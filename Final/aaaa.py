sinif=[[123,'ahmet gel',10],[234,'mehmet git',75],[345,'bahri dur',67],
   [567,'burcu koþ',83],[678,'berna yaz',56],[789,'binan yak',78]]
def siraliIsimler (sinif):
    x=[]
    y=[]
    for i in range(len(sinif)):
        x.append (sinif[i][2])
        y.append (sinif[i][2])
    for i in range(len(x)-1,0,-1):
        enyuksek=0
        for j in range(1,i+1):
            if x[j]<x[enyuksek]:
                enyuksek=j
        enyukseknot=x[i]
        x[i]=x[enyuksek]
        x[enyuksek]=enyukseknot
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]==y[j]:
                print sinif[j][1]
siraliIsimler(sinif)



