liste=["elma","armut","karpuz","kavun"]
while True:
    try:
        s=raw_input("L�tfen bit meyve ad� s�yleyiniz:")
        p=liste.index(s)+1
        print s,"listemizde",p,"nolu s�rada bulunuyor."
    except ValueError:
        pass
