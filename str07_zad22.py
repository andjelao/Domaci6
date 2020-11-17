n = int(input("Unesite koliko brojeva zelite da saberete: "))

def nadji_zbir(n):
    """
    ulazni parametar: broj n -> oznacava n cijelih brojeva
    returns njihov zbir
    """
    unos = 0
    zbir = 0
    while unos < n:
        broj = int(input("Unesite zeljeni broj: "))
        unos = unos + 1
        zbir = zbir + broj   
    return zbir
print(nadji_zbir(n))
