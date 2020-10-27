r = int(input("Unesite poluprecnik kruga: "))

def obim_i_povrsina_kruga(r):
    """
    ulazni parametri: poluprecnik kruga r
    returns obim i povrsina
    """
    pi = 3.14
    obim = 2 * r * pi
    povrsina = r * r * pi
    return obim, povrsina
print(obim_i_povrsina_kruga(r))