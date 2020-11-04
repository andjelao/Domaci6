n = int(input("Unesite neki cetvorocifreni broj: "))
def zamjena_trece_i_druge_cifre(n):
    """
    ulazni parametri: cetvorocifreni broj n
    returns broj koji nastaje zamjenom trece i druge cifre broja n
    """
    prva_cifra = n // 1000
    druga_cifra = (n // 100) % 10
    treca_cifra = (n // 10) % 10
    cetvrta_cifra = n % 10
    return prva_cifra * 1000 + treca_cifra * 100 + druga_cifra * 10 + cetvrta_cifra
print(zamjena_trece_i_druge_cifre(n))