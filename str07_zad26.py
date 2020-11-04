n = int(input("Unesite neki broj: "))

def je_prost(n):
    """
    ulazni parametri: broj n
    returns boolean da li je broj prost
    """
    djelilac = 2
    while djelilac < n:
        if n % djelilac == 0:
            return False
        djelilac = djelilac + 1
    return True
    
print(je_prost(n))
