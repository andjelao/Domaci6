c = int(input("Unesite rastojanje u centimetrima: "))

def cijelih_metara_u_rastojanju(c):
    """
    ulazni parametar: rastojanje u centimetrima c
    returns koliko cijelih metara ima u rastojanju
    """
    return c // 100
print(cijelih_metara_u_rastojanju(c))