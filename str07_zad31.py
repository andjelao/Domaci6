n = int(input("Unesite neki broj: "))

def is_Hemming(n):
    """
    ulazni parametar: broj n
    returns boolean da li je broj n Hemingvejov broj -> ako su mu prosti djelioci iz skupa {2, 3, 5}
    """
    lista = prosti_djelioci(n)
    skup = [2, 3, 5]
    for x in range(len(lista)):
        if lista[x] not in skup:
            return False
    return True

def prosti_djelioci(n):
    """
    ulazni parametar : broj n
    stampa sve proste djelioce broja n
    """
    djelioci = [ ]
    djelilac = 2
    while djelilac <= n:
        if n % djelilac == 0:
            if je_prost(djelilac):
                djelioci.append(djelilac)
        djelilac = djelilac + 1
    return djelioci

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
print(is_Hemming(n))