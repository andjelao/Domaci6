n = int(input("Unesite zeljeni broj: "))

def nadji_najveci(n):
    """
    ulazni parametar : broj n
    unose se brojevi sve dok se ne unese nula
    returns najveci od unesenih brojeva
    """
    lista = []
    while n != 0:
        lista.append(n)
        n = int(input("Unesite zeljeni broj: "))
    return max(lista)
print(nadji_najveci(n))

        
    

