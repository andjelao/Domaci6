a1 = 543
b1 = 130
a = 65

def koliko_se_kvadrata_moze_izrezati_iz_pravougaonika(a1, b1, a):
    """
    ulazni parametri: a1 i b1 -> stranice pravougaonika
                                 a -> stranica kvadrata
    returns koliko se kvadrata stranice a moze izrezati iz pravougaonika stranica a i b
    """
    povrsina_pravougaonika = a1 * b1
    povrsina_kvadrata = a * a
    return povrsina_pravougaonika // povrsina_kvadrata

print(koliko_se_kvadrata_moze_izrezati_iz_pravougaonika(a1, b1, a))