kromozom=[0,0,1,1,0,1,0,1]
def kanser(kromozom):
    s = " "
    i = 0
    while i < len(kromozom)-2:
        veri = kromozom[i:i+2]
        if veri == "00":
            s= s +"A"
        elif veri == "11":
            s= s+"T"
        elif veri == "01":
            s= s+"C"
        else:
            s= s+"G"
        i=i+2
    j=0
    while j < len(s)-1:
        veri2 = s[j:j+4]
        if veri2 == "ATCG":
            print("Pankreas Kanseri")
            return
        elif veri2 == "ATCC":
            print("iyi Huylu Kanser")
            return
        else:
            print("Kanser tehdidi yok")
            return
        j=j+1
kanser(kromozom)



