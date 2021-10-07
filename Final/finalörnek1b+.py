bit=[15,16,15,14,16,15,15,14]
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
