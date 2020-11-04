n = int(input("Unesite zeljeni broj: "))

def zbir_cifara(n):
    """
    ulazni parametar: broj n
    return zbir cifara broja n
    """
    suma = 0
    while n > 0:
        cifra = n % 10
        n = n // 10
        suma = suma + cifra
    return suma
print(zbir_cifara(n))
