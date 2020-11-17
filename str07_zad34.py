a = int(input("Unesite pocetak prvog zatvorenog intervala [a,b]: "))
b = int(input("Unesite kraj prvog zatvorenog intervala [a,b]: "))
c = int(input("Unesite pocetak drugog zatvorenog intervala [c,d]: "))
d = int(input("Unesite kraj drugog zatvorenog intervala [c,d]: "))

while a > b or c > d:
    print("Napravili ste gresku, unesite ponovo: ")
    a = int(input("Unesite pocetak prvog zatvorenog intervala [a,b]: "))
    b = int(input("Unesite kraj prvog zatvorenog intervala [a,b]"))
    c = int(input("Unesite pocetak drugog zatvorenog intervala [c,d]"))
    d = int(input("Unesite kraj drugog zatvorenog intervala [c,d]"))

def unija_intervala(a, b, c, d):
    """
    ulazni parametri: a -> pocetak prvog zatvorenog intervala [a,b]
                      b -> kraj prvog zatvorenog intervala [a,b]
                      c -> pocetak drugog zatvorenog intervala [c,d]
                      d -> kraj drugog zatvorenog intervala [c,d]
    returns duzinu intervala unije intervala
    """
    prvi_interval = []
    drugi_interval = []
    unija = []
    for x in range(a, b+1):
        prvi_interval.append(x)
    for y in range(c, d+1):
        drugi_interval.append(y)
    unija.extend(prvi_interval)
    unija.extend(drugi_interval)
    unija = set(unija)
    print(len(unija))

unija_intervala(a, b, c, d)


