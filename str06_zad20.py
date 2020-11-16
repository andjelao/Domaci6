n = int(input("Unesite ocjenu: "))

def prosjek_ocjena(n):
    suma = 0
    broj = 0
    while n > 0:
        suma = suma + n
        broj = broj + 1
        n = int(input("Unesite ocjenu: "))
    else:
        if n == 0:
            return suma / broj
        else:
            return 0
print(prosjek_ocjena(n))
