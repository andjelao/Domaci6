n = int(input("Unesite zeljeni trocifreni broj: "))

def zamjena_prve_i_poslednje_cifre(n):
    """
    ulazni parametar: trocifreni broj n
    returns broj koji se dobija zamjenom prve i poslednje cifre
    """
    prva_cifra = n // 100
    druga_cifra = (n // 10) % 10
    zadnja_cifra = n % 10
    return zadnja_cifra * 100 + druga_cifra * 10 + prva_cifra
print(zamjena_prve_i_poslednje_cifre(n))