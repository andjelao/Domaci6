n = int(input("Unesite zeljeni broj: "))

def isAmsgtrong(n):
    """
    ulazni parametar: broj n
    boolean returns da li je broj Amstrongov -> jednak zbiru kubova svojih cifara
    """
    broj = n
    suma = 0
    while broj > 0:
        cifra = broj % 10
        broj = broj // 10
        suma = suma + cifra ** 3
    return n == suma
print(isAmsgtrong(n))