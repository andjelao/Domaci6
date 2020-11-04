godina = int(input("Unesite zeljenu godinu: "))
def je_li_godina_prestupna(godina):
     """
     ulazni parametar : godina
     godina je prestupna ako : - je djeljiva sa 4
                               - nije djeljiva sa 100
                               - jeste djeljiva sa 400
     returns boolean da li je godina prestupna
     """
     return (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0
print(je_li_godina_prestupna(godina))
                 