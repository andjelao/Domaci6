a = int(input("Unesite pocetak zatvorenog intervala: "))
b = int(input("Unesite kraj zatvorenog intervala: "))

while a > b:
    print("Napravili ste gresku. Unesite ponovo: ")
    a = int(input("Unesite pocetak zatvorenog intervala: "))
    b = int(input("Unesite kraj zatvorenog intervala: "))
       
def prost_interval(a, b):
    """
    ulazni parametri: a -> pocetak zatvorenog intervala
                      b -> kraj zatvorenog intervala
    stampa sve proste brojeve iz intervala [a, b]
    """
    x = a
    while x <= b:
        if je_prost(x):
            print(x)
        x = x + 1   
def je_prost(n):
    """
    ulazni parametri: broj n
    returns boolean da li je broj prost
    """
    if n == 0 or n == 1:
        return False
    else:
        djelilac = 2
        while n % djelilac != 0:
            djelilac = djelilac + 1
        return djelilac == n
prost_interval(a, b)

     


