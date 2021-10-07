#list of alphabets
alfabe=["a","b","c","d","e","f","i","j","o"]

#function that filters vowels
del filtersesli(alfabe):
    sesliler=["a","e","i","o"]

    if (alfabe in sesliler):
        return True
    else:
        return False
filtersesli=filter(filtersesli,alfabe)
print("Filtrelenen sesli harfler:")
for ses in filtersesli:
    print(ses)
