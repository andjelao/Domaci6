palindrom = input("Unesite rijec koju zelite da provjerite: ")

def bezglasni_palindrom(palindrom):
    """
    ulazni parametar: string koji unosi korisnik
    u rijeci uzmemo prvo suglasnik i zamijenimo ga sa poslednjim suglasnikom, drugi suglasnik sa pretposlednjim...
    returns da li nakon tih operacija dobijemo istu rijec
    """
    lista1 = []
    lista2 = []
    for a in palindrom:
        lista1.append(a)
        lista2.append(a)
    x = 0
    y = len(lista2) - 1
    while x <= y:
        if lista2[x] not in ("a", "e", "i", "o", "u"):
            prvi_suglasnik = lista2[x]
            if lista2[y] not in ("a", "e", "i", "o", "u"):
                drugi_suglasnik = lista2[y]
                lista2[x] = drugi_suglasnik
                lista2[y] = prvi_suglasnik
                x = x + 1
                y = y - 1
            else:
                y = y - 1
        else:
            x = x + 1
    return lista1 == lista2
print(bezglasni_palindrom(palindrom))