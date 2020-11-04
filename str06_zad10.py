n = int(input("Unesite neki broj: "))

def min_max_cifra(n):
    """
    ulazni parametar: broj n
    returns zbir najmanje i najvece cifre tog broja
    """
    najmanja = 10
    najveca = 0
    while n > 0:
        cifra = n % 10
        n = n // 10
        if cifra < najmanja:
            najmanja = cifra
        if cifra > najveca:
            najveca = cifra
    return najmanja + najveca
print(min_max_cifra(n))