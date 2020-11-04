n = int(input("Unesite broj:"))

def najveca_cifra(n):
    """
    ulazni parametar: broj n
    returns najvecu cifru tog broja
    """
    najveca = 0
    while n > 0:
        cifra = n % 10
        n = n // 10
        if cifra > najveca:
            najveca = cifra
    return najveca
print(najveca_cifra(n))
