x = int(input("Unesite vrijednost x: "))

def manji_od_x(x):
    """
    ulazni parametar : broj x
    ucitava cijele brojeve dok se ne ucita broj koji je veci od x
    stampa broj ucitanih brojeva, broj ucitanih parnih brojeva i zbir svih ucitanih brojeva
    """
    broj = 0
    suma = 0
    broj_parnih = 0
    while broj <= x:
        suma = suma + broj
        if broj % 2 == 0:
            broj_parnih = broj_parnih + 1
        broj = broj + 1
    ucitani = x + 1
    print("parni:",broj_parnih,"zbir:",suma,"broj ucitanih:",ucitani)

manji_od_x(x)