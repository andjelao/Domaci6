x = int(input("Unesite broj x: "))
a = int(input("Unesite broj a: "))
def promjena(x, a):
    """
    ulazni parametar: brojevi x i a
    returns a * x ako je x nenegativno
    returns a / x ako je x negativno
    """
    if x >= 0:
        return a * x
    else: 
        return a / x
print(promjena(x, a))