n = int(input("Unesite zeljeni broj: "))

def najveci_neparni_djelilac(n):
    """
    ulazni parametar: broj n
    returns najveci neparni djelilac broj
    """
    djelilac = 1
    najveci_djelilac = 1
    while djelilac <= n:
        if n % djelilac == 0:
            if djelilac % 2 == 1:
                if djelilac > najveci_djelilac:
                    najveci_djelilac = djelilac
        djelilac = djelilac + 1
    return najveci_djelilac
print(najveci_neparni_djelilac(n))