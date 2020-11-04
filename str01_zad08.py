
a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))

def da_li_je_djeljiv(a,b):
    """
    ulazni parametri: brojevi a i b
    ispituje da li je a djeljivo sa b i stampa poruku: "a je djeljivo sa b" ili "a nije djeljivo sa b"
    """
    if a % b == 0:
        print(a,"je djeljivo sa", b)
    else: 
        print(a, "nije djeljivo sa", b)

da_li_je_djeljiv(a,b)
