h = int(input("Unesite broj molekula vodonika: "))
s = int(input("Unesite broj molekula sumpora: "))
o = int(input("Unesite broj molekula kiseonika: "))

def kiselina(h, s, o):
    """
    ulazni parametri: h -> broj molekula vodonika
                      s -> broj molekula sumpora
                      o -> broj molekula kiseonika
    returns koliko se najvise molekula sumporne kiseline H2SO4 moze dobiti od datih molekula
    """
    broj_kiselina = 0
    while h - 2 > 0 and o - 4 > 0 and s - 1 > 0:
        broj_kiselina = broj_kiselina + 1
        h = h - 2 
        s = s - 1
        o = o - 4
    return broj_kiselina
print(kiselina(h, s, o))