print("Unesite sljedece podatke o trapezu: ")
a = int(input("osnovica a: "))
b = int(input("osnovica b: "))
h = int(input("visina h: "))

def povrsina_trapeza(a, b, h):
    """
    ulazni parametri: osnovice trapeza a i b, i visina h
    returns povrsina
    """
    return ((a+ b) * h) / 2
print(povrsina_trapeza(a, b, h))
