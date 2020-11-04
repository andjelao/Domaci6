n = int(input("Unesite neki cetvorocifreni broj: "))
def zbir_kvadrata_cifara(n):
    """
    ulazni parametar: cetvorocifreni broj n
    returns zbir kvadrata cifara broja n
    """
    suma = 0
    while n > 0:
        cifra = n % 10
        n = n // 10
        suma = suma + cifra **2
    return suma
print(zbir_kvadrata_cifara(n))