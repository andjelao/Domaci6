a = int(input("Unesite donju granicu zatvorenog intervala: "))
b = int(input("Unesite gornju granicu zatvorenog intervala: "))
def print3k(a, b):
    """
    ulazni parametri : broj a -> donja granica zatvorenog intervala
                       broj b -> gornja granica zatvorenog intervala 
    returns broj 3 * k + 1 koji pripada ovom intervalu
    """
    k = 1
    x = 3 * k + 1
    while x >= a and x <= b:
        print(x)
        k = k + 1
        x = 3 * k + 1
print3k(a, b)
