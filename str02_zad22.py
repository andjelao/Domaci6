import math
print("Unesite koordinate tacke A: ")
a1 = int(input("x: "))
a2 = int(input("y: "))
print ("Unesite koordinate tacke B: ")
b1 = int(input("x: "))
b2 = int(input("y: "))
print("Unesite koordinate tacke C: ")
c1 = int(input("x: "))
c2 = int(input("y: "))
print("Unesite koordinate tacke D: ")
d1 = int(input("x: "))
d2 = int(input("y: "))

def da_li_je_pravougaonik(a1, a2, b1, b2, c1, c2, d1, d2):
    """
    ulazni parametar: matrica sa 4 niza od po 2 elementa -> 4 tacke pravougaonika sa svoje 2 koordinate
    pravougaonik postoji ako ima dva para jednakih i paralelnih stranica, i ako ima sve prave uglove
    returns boolean da li postoji pravougaonik odredjen ovim tackama
    """
    boolean = False
    if math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2) == math.sqrt((d1 - c1) ** 2 + (d2 - c2) ** 2):
        if math.sqrt((c1 - b1) ** 2 + (c2 - b2) ** 2) == math.sqrt((d1 - a1) ** 2 + (d2 - a2) ** 2): 
            if a2 == b2:
                if d2 == c2:
                    if a1 == d1:
                        if b1 == c1:
                            boolean = True
    return boolean
print(da_li_je_pravougaonik(a1, a2, b1, b2, c1, c2, d1, d2))


                    