n = int(input("Unesite broj n: "))

def nadji_zbir(n):
    """
    ulazni parametar: broj n -> oznacava n cijelih brojeva
    returns njihov zbir
    """
    zbir = 0
    for x in range(n):
        zbir = zbir + x
    return zbir
print(nadji_zbir(n))
