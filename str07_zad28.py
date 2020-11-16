n = int(input("Unesite neki broj: "))

def prosti_djelioci(n):
    """
    ulazni parametar : broj n
    stampa sve proste djelioce broja n
    """
    djelilac = 2
    while djelilac <= n:
        if n % djelilac == 0:
            if je_prost(djelilac):
                print(djelilac)
        djelilac = djelilac + 1

def je_prost(n):
    """
    ulazni parametri: broj n
    returns boolean da li je broj prost
    """
    if n == 0 or n == 1:
        return False
    else:
        djelilac = 2
        while n % djelilac != 0:
            djelilac = djelilac + 1
        return djelilac == n
prosti_djelioci(n)