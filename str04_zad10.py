import math
r = int(input("Unesite poluprecnik kupe: "))
H = int(input("Unesite visinu kupe: "))

def povrsina_i_zapremina_kupe(r, H):
    """
    ulazni parametri: poluprecnik osnove kupe r i visina kupe H
    returns povrsinu i zapreminu
    """
    pi = 3.14
    s = math.sqrt(H * H + r * r)
    povrsina = r * pi * (r + s)
    zapremina = (r * r * pi * H) / 3
    return povrsina, zapremina
print(povrsina_i_zapremina_kupe(r, H))
