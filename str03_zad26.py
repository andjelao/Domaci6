"""
Data je meta sa 10 koncentricnih krugova sa centrom u koordinatnom pocetku i 3 tacke A1(x1, y1), A2(x2, y2) i A3(x3, y3).
Za pogodak u najmanji krug dobija se 10 bodova, za svaki od sljedecih krugova po jedan bod manje a za pogodak van mete dobija se
0 bodova. Napisati program koji ocitava koordinate tacaka A1, A2, i A3 i stampa ukupan broj bodova koji donose pogoci u tacke A1, A2, i A3 
"""
import math 
r = int(input("Unesite poluprecnik najmanjeg kruga: "))
x1 = int(input("Unesite x koordinatu tacke A1: "))
y1 = int(input("Unesite y koordinatu tacke A1: "))
x2 = int(input("Unesite x koordinatu tacke A2: "))
y2 = int(input("Unesite y koordinatu tacke A2: "))
x3 = int(input("Unesite x koordinatu tacke A3: "))
y3 = int(input("Unesite y koordinatu tacke A3: "))

def meta(r, x1, y1, x2, y2, x3, y3):
    #racunamo da je centar svake kruznice 
    #poluprecnik najmanje kruznice je r, a svake sledece je broj_kruznice*r
    lista = [(x1, y1), (x2, y2), (x3, y3)]
    broj_bodova = 0
    for x in lista:
        broj_kruznice = 1
        rastojanje_od_centra = math.sqrt((0 - x[0])**2 + (0 - x[1])**2)
        while broj_kruznice <= 10:
            if rastojanje_od_centra <= broj_kruznice * r:
                broj_bodova = broj_bodova + 10 - (broj_kruznice - 1)
                break
            else:
                broj_kruznice = broj_kruznice + 1
    return broj_bodova
print(meta(r, x1, y1, x2, y2, x3, y3))


