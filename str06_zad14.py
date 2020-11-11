n = int(input("Unesite zeljeni broj: "))
def stepen_dvojke(n):
    """
    ulazni parametar: broj n
    returns boolean da li je n stepen dvojke
    """
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            return False
    return True
print(stepen_dvojke(n))