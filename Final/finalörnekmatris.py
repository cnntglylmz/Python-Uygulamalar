test=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
max_sutun=len(test)
max_satir=len(test[0])
sutun=[[]for i in range(max_sutun)]
satir=[[]for i in range(max_satir)]
fkose=[[]for i in range(max_sutun+max_satir-1)]
bkose=[[]for i in range(len(fkose))]
min_bkose=-max_satir+1
for y in range(max_sutun):
    for x in range(max_satir):
        sutun[y].append(test[y][x])
        satir[x].append(test[y][x])
        fkose[x+y].append(test[y][x])
        bkose[-min_bkose+x-y].append(test[y][x])
print (sutun)
print (satir)
print (fkose)
print (bkose)
