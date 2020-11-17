n = int(input("Unesite prvi broj: "))
m = int(input("Unesite drugi broj: "))

def gcd(n, m):
    """
    ulazni parametri : brojevi n i m
    pomocu euklidovog algoritma racuna najveci zajednicki djelilac -> nzd
    returns nzd
    """
    if n < m:
        n, m = m, n
    djelilac = m
    ostatak = n % m
    while ostatak != 0:
        djelilac = ostatak
        ostatak = n % djelilac
    return djelilac

print(gcd(n, m))