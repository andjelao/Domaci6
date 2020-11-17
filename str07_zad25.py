import math
n = int(input("Koliko trouglova zelite da provjerite? "))

def nadji_najveci_trougao(n):
    """
    ulazni parametar : broj trouglova n
    unose se stranice a, b i c n trouglova
    returns povrsinu najveceg trougla
    """
    unos = 0
    povrsine = []
    while unos != n:
        a = int(input("Unesite stranicu a: "))
        b = int(input("Unesite stranicu b: "))
        c = int(input("Unesite stranicu c: "))
        povrsina = povrsina_trougla(a, b, c)
        povrsine.append(povrsina)
        unos = unos + 1
    return max(povrsine)

def povrsina_trougla(a, b, c):
    s = (a + b + c) / 2
    povrsina = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return povrsina
print(nadji_najveci_trougao(n))
