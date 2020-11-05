k = int(input("Unesite jedan cijeli broj od 1 do 180: "))
while k < 1 or k > 180:
   k = int(input("Unesite jedan cijeli broj od 1 do 180: "))
def cifre_broja(k):
    """
ulazni parametar: cijeli broj k
niz -> svi dvocifreni brojevi
returns dvocifreni broj koji sadrzi k-tu cifru u datom nizu
    """
    x = 10
    niz = []
    while x < 100:
        niz.append(x // 10)
        niz.append(x % 10)
        x = x + 1
    if k % 2 == 0:
        return niz[k] * 10 + niz[k+1]
    else:
        return niz[k-1] * 10 + niz[k]

print(cifre_broja(k))