a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
c = int(input("Unesite treci broj: "))

def najveci_od_tri_broja(a, b, c):
    """
    ulazni parametri- tri broja
    returns najveci od njih
    """
    if a > b:
        if b > c:
            return a
        elif a > c:
            return a
        else: 
            return c
    else:
        if a > c:
            return b
        elif b > c:
            return b
        else:
            return c
    
print(najveci_od_tri_broja(a, b, c))