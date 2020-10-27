import math
x = float(input("Unesite x koordinatu tacke: "))
y = float(input("Unesite y koordinatu tacke: "))

def koordinate_tacke_A():
    """
    dat poluprecnik veceg kruga r = 6
    tacka A(xa, ya) -> tacka presjeka prave x - y - 4 = 0 i kruzne linije vece kruznice x * x + y * y = 36
    izrazimo x = y + 4 iz jednacine prave
    zamijenimo x u jednacinu kruzne linije
    dobijemo kvadratnu jednacinu y * y + 4 * y - 5 = 0
    pomocu koeficijenata a, b i c ove kvadratne jednacine racunamo njena rjesenja y1 i y2 -> postoje dvije presjecne tacke
    postavljamo uslov da rjesenje mora da bude vece od nule jer se nasa trazena tacka nalazi u pozitivnom dijelu y ose
    returns y koordinatu A tacke
    """
    a = 1
    b = 4
    c = -5
    y1 = (-b + math.sqrt(b ** 2 - 4 * a * c )) / 2 * a
    y2 = (-b - math.sqrt(b ** 2 - 4 * a* c )) / 2 * a
    if y1 > 0:
        y = y1
    else: 
        y = y2
    return y

def da_li_pripada_ravni(x, y):
    """
    ulazni parametri: x i y koordinate tacke
    returns boolean pripada da li tacka pripada osjencenom dijelu ravni
    """
    pripada = False
    rastojanje_od_centra = math.sqrt((0 - x)**2 + (0 - y)**2)
    if x - y - 4 != 0:
        if rastojanje_od_centra > 4 and rastojanje_od_centra < 6:
            if y > 0:
                if x < 0:
                    pripada = True
                elif x > 0:
                    ya = koordinate_tacke_A()
                    if y < ya:
                        pripada = True
        elif rastojanje_od_centra < 4:
            if x > 0:
                if y > 0:
                    pripada = True
                elif y < 0:
                    # u formulu za rastojanje tacke od prave uvrstimo x i y koordinate koordinantog pocetka i jednacinu prave x-y-4=0
                    a = 1
                    b = -1
                    c = -4
                    x0 = 0
                    y0 = 0
                    rastojanje_prave_od_centra = abs(a * x0 - b * y0 + c) / math.sqrt(a * a + b * b)
                    if rastojanje_od_centra > rastojanje_prave_od_centra:
                        pripada = True
    return pripada

print(da_li_pripada_ravni(x, y))

