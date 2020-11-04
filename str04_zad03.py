a = int(input("Unesite duzinu stranice a pravougaonika: "))
b = int(input("Unesite duzinu stranice b pravougaonika: "))

def obim_i_povrsina_pravougaonika(a, b):
    """
    ulazni parametri: stranice pravougaonika a i b
    returns obim i povrsina
    """
    obim = 2 * (a + b)
    povrsina = a * b
    return obim, povrsina
print(obim_i_povrsina_pravougaonika(a, b))