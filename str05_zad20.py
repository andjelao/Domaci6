datum = input("Unesite datum u obliku dd.mm.gg. : ")
rodjendan = input("Unesite rodjendan u obliku dd.mm. : ")

def dani_do_rodjendana(datum, rodjendan):
    """
    ulazni parametri: string datum -> od njega mjerimo koliko dana je ostalo do rodjendana
                      string rodjendan -> dan i mjesec rodjendana
    returns za koliko dana od unesenog datuma je rodjendan
    """
    datum = datum.split(".")
    dan = int(datum[0])
    mjesec = int(datum[1])
    godina = int(datum[2])

    rodjendan = rodjendan.split(".")
    dan_rodjendana = int(rodjendan[0])
    mjesec_rodjendana = int(rodjendan[1]) 

    dani_u_mjesecu = [31, 27, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    redni_broj_dana = 0
    redni_broj_rodjendana = 0
    if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
        broj_dana_u_godini = 366
        dani_u_mjesecu[1] = 28
    else:
        broj_dana_u_godini = 365
    #da odredimo redni broj danasnjeg datuma u godini
    for x in range(len(dani_u_mjesecu)):
        if mjesec - 1 > x:
            redni_broj_dana = redni_broj_dana + dani_u_mjesecu[x]
    redni_broj_dana = redni_broj_dana + dan
    
    # da odredimo redni broj rodjendana u godini
    for x in range(len(dani_u_mjesecu)):
        if mjesec_rodjendana - 1 > x:
            redni_broj_rodjendana = redni_broj_rodjendana + dani_u_mjesecu[x]
    redni_broj_rodjendana = redni_broj_rodjendana + dan_rodjendana

    if redni_broj_rodjendana > redni_broj_dana:
        do_rodjendana = redni_broj_rodjendana - redni_broj_dana
    elif redni_broj_dana == redni_broj_rodjendana:
        print("Srecan rodjendan!!!")
        do_rodjendana = 0
    else:
        do_rodjendana = (broj_dana_u_godini - redni_broj_dana) + redni_broj_rodjendana
    return do_rodjendana

print(dani_do_rodjendana(datum, rodjendan))
