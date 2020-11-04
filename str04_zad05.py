v = int(input("Unesite zapreminu tijela: "))
m = int(input("Unesite masu tijela: "))

def gustina_tijela(v, m):
    """
    ulazni parametri: zapremina i masa tijela
    returns gustina
    """
    return m / v
print(gustina_tijela(v, m))