a = int(input("Unesite pocetak intervala: "))
b = int(input("Unesite kraj intervala: "))
x = int(input("Unesite broj koji zelite da provjerite: "))
def da_li_pripada_intervalu(a, b, x):
    """
    ulazni parametri: a -> donja granica zatvorenog intervala [a, b]
                      b -> gornja granica zatvorenog intervala [a, b]
    returns boolean da li broj x pripada ovom intervalu
    """
    if x >= a:
        if x <= b:
            return True
    return False
print(da_li_pripada_intervalu(a, b, x))