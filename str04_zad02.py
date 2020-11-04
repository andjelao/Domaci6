a = int(input("Unesite duzinu stranice a: "))

def obim_i_povrsina_kvadrata(a):
    """
    ulazni parametar: duzina stranice kvadrata a
    returns obim i povrsinu
    """
    obim = 4 * a
    povrsina = a * a
    return obim, povrsina

print(obim_i_povrsina_kvadrata(a)) 