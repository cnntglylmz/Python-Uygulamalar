dizi=[[1,0,0,0,0],[1,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,1,1,1]]
def yolbul(dizi):
    for i in range (len(dizi)):
        for j in range (len(dizi)):
            print dizi[i][j],
        print
    for i in range (len(dizi)):
        for j in range (len(dizi)):
            if dizi[i][j]==1:
                yol=[]
                yol.append(dizi[i][j])
                yol=[i]+[j]
                print yol
yolbul(dizi)
