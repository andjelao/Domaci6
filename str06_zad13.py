n = int(input("Unesite neki broj: "))

def faktorijal(n):
    """
    ulazni parametar: broj n
    rekurzivna funkcija returns faktorijal broja n
    """
    if n == 1:
        return 1
    else: 
        return n * faktorijal(n - 1)
print(faktorijal(n))