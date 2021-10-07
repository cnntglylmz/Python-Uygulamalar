liste=["elma","armut","karpuz","kavun"]
while True:
    try:
        s=raw_input("Lütfen bit meyve adý söyleyiniz:")
        p=liste.index(s)+1
        print s,"listemizde",p,"nolu sýrada bulunuyor."
    except ValueError:
        pass
