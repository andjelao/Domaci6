"""
Dva automobila se krecu po kruznoj stazi duzine L u suprotnim smjerovima. Polaze iz iste tacke i krecu se stalnim brzinama v1 i v2.
Na kom rastojanju ce se naci autimobil u trenutku T? 
Ulaz : u jednom redu zadaju se 4 cijela broja L, v1, v2, T razdvojeni blankom (1 <= L, v1, v2, T <= 100) 
"""
unos = input("Unesite duzinu staze, brzinu1, brzinu2, i trenutak : ")

def rastojanje(unos):
    lista = unos.split(" ")
    L = int(lista[0])
    v1 = int(lista[1])
    v2 = int(lista[2])
    T = int(lista[3])
    while T > 100:
        T = int(input("Napravili ste gresku, unesite ponovo T tako da bude vece ili jednako 100: "))
    else: 
        s1 = v1 * T #predjeni put automobila1
        s2 = v2 * T #predjeni put automobila2
        return s1 + s2

print(rastojanje(unos))
