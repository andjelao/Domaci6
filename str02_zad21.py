import math
print("Unesite koordinate tacke A: ")
a1 = int(input("x: "))
a2 = int(input("y: "))
print("Unesite koordinate tacke B: ")
b1 = int(input("x: "))
b2 = int(input("y: "))
print("Unesite koordinate tacke C: ")
c1 = int(input("x: "))
c2 = int(input("y: "))

def visine_trougla(a1, a2, b1, b2, c1, c2):
    """
    ulazni parametri: x i y koordinate tacaka A, B, i C
    provjerava da li trougao odredjenim ovim tackama postoji pomocu formule za povrsinu trougla preko koordinata tacaka
    racuna duzinu stranica trougla
    kombinujuci dvije formule za povrsinu trougla racuna odgovarajuce visine
    returns visine trougla ha, hb, hc
    
    """
    povrsina = (abs(a1 * (b2 - c2) + b1 * (c2 - a2) + c1 * (a2 - b2))) / 2
    if povrsina != 0:
        a = math.sqrt((c1 - b1) ** 2 + (c2 - b2) ** 2)
        b = math.sqrt((c1 - a1) ** 2 + (c2 - a2) ** 2)
        c = math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2)
        ha = (2 * povrsina) / a
        hb = (2 * povrsina) / b
        hc = (2 * povrsina) / c
        return ha, hb, hc
print(visine_trougla(a1, a2, b1, b2, c1, c2))