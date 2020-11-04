a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

def zbir_iz_intervala(a, b):
    """
    ulazni parametri: granice zatvorenog intervala [a, b]
    returns zbir svih brojeva iz ovog intervala
    """
    suma = 0
    for x in range(a, b+1):
        suma = suma + x
    return suma
print(zbir_iz_intervala(a, b))


