a = int(input("Unesite prvi cijeli broj: "))
b = int(input("Unesite drugi cijeli broj: "))
c = int(input("Unesite treci cijeli broj: "))

def barem_jedan_parni_i_neparan_broj(a, b, c):
    """
    ulazni parametri: cijeli brojevi a, b i c koje unosi korisnik
    returns boolean da li medju njima ima barem jedan parni i barem jedan neparni broj
    """
    parni = 0
    neparni = 0
    niz = [a, b, c]
    for i in range(len(niz)):
        if niz[i] % 2 == 0 :
            parni = parni + 1
        else:
            neparni = neparni + 1
    if parni >= 1 and neparni >= 1:
        print("Yes")
    else:
        print("No")
barem_jedan_parni_i_neparan_broj(a, b, c)
