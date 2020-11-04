povrsina = int(input("Unesite povrsinu drzave: "))
broj_stanovnika = int(input("Unesite broj stanovnika drzave: "))

def gustina_naseljenosti_drzave(povrsina, broj_stanovnika):
    """
    ulazni parametri: povrsina drzave, broj stanovnika
    returns gustina naseljenosti
    """
    return broj_stanovnika / povrsina
print(gustina_naseljenosti_drzave(povrsina, broj_stanovnika))
