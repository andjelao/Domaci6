x = float(input("Unesite vrijednost x: "))
eps = float(input("Unesite vrijednost eps: "))

def red_EX(x, eps):
    """
    ulazni parametar : float x i float eps koje unosi korisnik
    racuna vrijednost zbira reda x^n / n!
    sumiranje se prekida kada tekuci sabirak po apsolutnoj vrijednosti postane ne veci od vrijednosti eps
    returns zbir
    """
    n = 0
    zbir = 0
    sabirak = (x ** n) / faktorijal(n)
    while abs(sabirak) > eps:
        zbir = zbir + sabirak
        n = n + 1
        sabirak = (x ** n) / faktorijal(n)
    return zbir

def faktorijal(n):
    """
    ulazni parametar: broj n
    rekurzivna funkcija returns faktorijal broja n
    """
    if n == 0 or n == 1:
        return 1
    else: 
        return n * faktorijal(n - 1)

print(red_EX(x, eps))