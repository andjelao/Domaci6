import math
print("Unesite koordinate tacke A: ")
x1 = int(input("x: "))
y1 = int(input("y: "))
x2 = int(input("x: "))
y2 = int(input("y: "))

def duzina_duzi(x1, y1, x2, y2):
    """
    ulazni parametri : koordinate tacaka A(x1, y1) i B(x2, y2)
    returns duzinu duzi odredjenu ovim tackama
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(duzina_duzi(x1, y1, x2, y2))
