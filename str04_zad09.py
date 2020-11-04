a = int(input("Unesite stranicu a kvadra: "))
b = int(input("Unesite stranicu b kvadra: "))
c = int(input("Unesite stranicu c kvadra: "))

def povrsina_i_zapremina_kvadra(a, b, c):
    """
    ulazni parametri: stranice kvadra a, b i c
    returns povrsinu i zapreminu
    """
    povrsina = 2 * (a * b + a * c + b * c)
    zapremina = a * b * c
    return povrsina, zapremina
print(povrsina_i_zapremina_kvadra(a, b, c))
