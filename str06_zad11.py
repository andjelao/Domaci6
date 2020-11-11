x = int(input("Unesite vrijednost osnove: "))
n = int(input("Unesite vrijednost stepena: "))
def stepen(x, n):
    """
    ulazni parametri: broj x -> osnova
                      broj n -> stepen broja x
    returns broj x na stepen n
    """
    if n == 0:
        return 1
    else:
        rezultat = 1
        stepen = 1
        while stepen <= n:
            rezultat = rezultat * x
            stepen += 1
        return rezultat
print(stepen(x, n))
