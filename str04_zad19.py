zbir = int(input("Unesite zbir: "))

def broj_golova_na_utakmici(zbir):
    """
    ulazni parametar: zbir golova na utakmici
    returns koliko je golova bilo na utakmici
    """
    umanjilac = 1
    gol = 0
    while(zbir > 0):
        zbir = zbir - umanjilac
        gol = gol + 1
        umanjilac = umanjilac + 1
    return gol
print(broj_golova_na_utakmici(zbir))
        