x = float(input("Unesite vrijednost x, tako da ona bude izmedju -1 i 1: "))
eps = float(input("Unesite vrijednost eps: "))

def red(x, eps):
    """
    ulazni parametar : float x i float eps koje unosi korisnik
    racuna vrijednost zbira reda (-1) ^ n * (n + 1) * x ^ 2 * n
    sumiranje se prekida kada tekuci sabirak po apsolutnoj vrijednosti postane manji od vrijednosti eps
    returns zbir
    """
    while x <= -1 or x >= 1:
        print("Nedozvoljena vrijednost x, pokusajte ponovo: ")
        x = float(input("Unesite vrijednost x, tako da ona bude izmedju -1 i 1: "))
    else:
        n = 0
        zbir = 0
        sabirak = ((-1) ** n ) * ((n + 1) * x ** (2 * n))
        while abs(sabirak) >= eps:
            zbir = zbir + sabirak
            n = n + 1
            sabirak = ((-1) ** n ) * ((n + 1) * x ** (2 * n))
        return zbir
print(red(x, eps))

