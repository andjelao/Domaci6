N = int(input("Unesite velicinu potpunog skupa domina: "))

def domine(N):
    """
    ulazni parametar : N -> broj tackica na jednoj plocici moze biti broj izmedju 0 i N, ukljucivo
    returns ukupan broj tackica na svim plocicama u potpunom skupu domina velicine N
    """
    x = 0
    y = 0
    broj_tackica = 0
    while x < N and y <= N:
        if x == y:
            x = 0
            y = y + 1
            broj_tackica = broj_tackica + y + x
        if y > x:
            x = x + 1 
            broj_tackica = broj_tackica + x + y
    return broj_tackica
print(domine(N))


