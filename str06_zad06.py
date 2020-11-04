n = int(input("Unesite neki broj: "))
def broj_djelilaca(n):
    """
    ulazni parametar: broj n
    returns broj pozitivnih djelilaca broja n
    """
    brojdjelilaca = 0
    djelilac = 1
    while djelilac <= n:
        if n % djelilac == 0:
            brojdjelilaca = brojdjelilaca + 1
        djelilac = djelilac + 1
    return brojdjelilaca
print(broj_djelilaca(n))