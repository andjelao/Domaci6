n = int(input("Unesite broj: "))
def spisak_djelilaca(n):
    """
    ulazni parametar : broj n
    stampa sve pozitivne djelioce broja n
    """
    djelilac = 1
    while djelilac <= n:
        if n % djelilac == 0:
            print(djelilac)
        djelilac = djelilac + 1
spisak_djelilaca(n)