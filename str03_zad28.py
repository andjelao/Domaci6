k = int(input("Unesite vrijednost k: "))
def fraza_k_pecuraka(k):
    """
    ulazni parametar: broj pecuraka k
    stampa frazu „Na izletu smo ubrali k pecuraka“ i prilagodjava oblik imenice pecurka broju ispred nje
    """
    c = k % 10
    if k >= 0 :
        if k >= 11 and k <= 19:
            rijec = "pecurki"
        elif c == 1:
            rijec = "pecurku"
        elif c != 0 and c < 5:
            rijec = "pecurke"
        else:
            rijec = "pecurki"
        print("Na izletu smo ubrali",k,rijec)
    else:
        print("Napravili ste gresku")
    
fraza_k_pecuraka(k)
