mjesec = int(input("Unesite broj mjeseca: "))
godina = int(input("Unesite godinu: "))

def broj_dana_u_mjesecu(mjesec, godina):
    """
    ulazni parametri : mjesec i godina
    returns broj dana u datom mjesecu, od toga da li je godina prestpuna zavisi koliko februar ima dana
    """
    while mjesec > 12:
        mjesec = int(input("Napravili ste gresku. Unesite broj mjeseca ponovo: "))
    else: 
        if mjesec == 1:
            print(31)
        elif mjesec == 2:
            if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
                print(29)
            else: 
                print(28)
        elif mjesec == 3:
            print(31)
        elif mjesec == 4:
            print(30)
        elif mjesec == 5:
            print(31)
        elif mjesec == 6:
            print(30)
        elif mjesec == 7:
            print(31)
        elif mjesec == 8:
            print(31)
        elif mjesec == 9:
            print(30)
        elif mjesec == 10:
            print(31)
        elif mjesec == 11:
            print(30)
        else:
            print(31)
broj_dana_u_mjesecu(mjesec, godina)
        