n = int(input("Unesite broj: "))

def zbir_djelilaca(n):
    """
    ulazni parametar : broj n
    returns zbir pozitivnih djelilaca broja n manjih od n
    """
    zbir = 0
    djelilac = 1
    while djelilac < n:
        if n % djelilac == 0:
            zbir = zbir + djelilac
        djelilac = djelilac + 1
    return zbir
print(zbir_djelilaca(n))