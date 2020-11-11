n = int(input("Unesite zeljeni broj: "))
def min_stepen_dvojke(n):
    """
    ulazni parametar : broj n
    returns najmanji prirodan broj k takav da n nije veci od broja 2 ^ k
    """
    k = 1
    x = 2 ** k
    while n >= x:
        k = k + 1
        x = 2 ** k
    return k
print(min_stepen_dvojke(n))