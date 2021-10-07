a=[[0,0,0,0,0,1,0,0],[0,0,0,1,0,1,0,0],[0,0,0,1,0,1,0,0],[1,0,0,1,0,1,1,1],[1,0,0,1,1,1,0,0],[1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
for i in range (len(a)):
    for j in range (len(a)):
        print a[i][j],
    print 
sayac=0
for j in range (len(a)-2):
    for i in range (len(a)-3):       
        if a[i][j]==1:
            if a[i+3][j+2]==1:
                if a[i+3][j+1]==1:
                    if a[i+3][j]==1:
                        if a[i+2][j]==1:
                            if a[i+1][j]==1:                                           
                                sayac=sayac+1
                               
print sayac
