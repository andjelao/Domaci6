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

def odrediti_tip_trougla(a1, a2, b1, b2, c1, c2):
    """
    ulazni parametri: koordinate tacaka trougla A(a1, a2), B(b1, b2), C(c1, c2)
    stampa tip trougla ABC: ostrougli/pravougli/tupogli 
    """
    c = (b1 - a1)**2 + (b2 - a2)**2
    a = (c1 - b1)**2 + (c2 - b2)**2
    b = (c1 - a1)**2 + (c2 - a2)**2 

    if c > a and c > b:
        najveca = c
        suma = a + b 
    elif a > b and a > c:
        najveca = a
        suma = c + b
    else:
        najveca = b
        suma = a + c
    if najveca == suma:
        print("Trougao je pravougli.")
    elif najveca > suma:
        print("Trougao je tupougli.")
    else: 
        print("Trougao je ostrougli.")
odrediti_tip_trougla(a1, a2, b1, b2, c1, c2)

