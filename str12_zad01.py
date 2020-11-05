simbol = input("Unesite simbol za koji provjeravate da li je cifra: ")
palindrom = input("Unesite rijec ili recenicu za koju zelite da provjerite da li je palindrom: ")
slovo = input("Unesite slovo za koje zelite da promijenite velicinu: ")
recenica = input("Unesite recenicu za koju zelite da provjerite broj rijeci: ")
string = input("Unesite rijec za koju provjeravate da li ima dva ista slova: ")
print("Provjera da li je drugi string substring prvog: ")
string1 = input("Unesite prvi string: ")
string2 = input("Unesite drugi string: ")
space_string = input("Unesite string iz kojeg zelite da izbrisete uzastopne space-ove: ")

def da_li_je_cifra(simbol):
    """
    ulazni parametar : simbol x koji unosi korisnik
    returns boolean da li je x cifra
    """
    if simbol.isdigit():
        simbol = int(simbol)
        return simbol < 10
    return False
def da_li_je_palindrom(palindrom):
    """
    ulazni parametar: string koji unosi korisnik
    ako string ima razmake izmedju rijeci uklanja ih
    returns boolean da li je rijec palindrom - cita se isto sa obje strane
    """
    palindrom = palindrom.replace(" ","")
    return palindrom == palindrom[::-1]
def promijeni_velicinu(slovo):
    """
    ulazni parametri: karakter slovo koje unosi korisnik
    ako je malo slovo -> vraca veliko
    ako je veliko slovo -> vraca malo
    """
    if slovo.islower():
        return slovo.upper()
    else:
        return slovo.lower()
def broj_rijeci_u_stringu(recenica):
    """
    ulazni parametar: string koji sadrzi praznine izmedju rijeci
    returns broj rijeci u stringu
    """
    broj_rijeci = recenica.split(" ")
    return len(broj_rijeci)
def najduza_rijec_u_stringu(recenica):
    """
    ulazni parametar: string koji sadrzi praznine izmedju rijeci
    returns najduzu rijec u stringu
    """
    rijeci = recenica.split(" ")
    rijec = rijeci[0]
    najduza = len(rijeci[0])
    for i in range (len(rijeci)):
        if len(rijeci[i]) > najduza:
            najduza = len(rijeci[i])
            rijec = rijeci[i]
    return rijec
def ista_slova(string):
    """
    ulazni parametri: rijec koja sadrzi dva ista slova
    returns slovo koje se ponavlja u rijeci
    """
    for i in range(len(string)):
        letter = string[i]
        for x in range(len(string)):
            if letter == string[x] and i != x:
                return letter
        x = 0
def substring(string1, string2):
    """
    ulazni parametri: string1 i string2 koje unosi korisnik
    returns boolean ako je string2 podstring stringa1
    """
    return string2 in string1
def space(space_string):
    """
    ulazni parametar: string koji sadrzi vise od jednog uzastopnog blanka
    returns string sa uklonjenim viskom blankova
    """
    while "  " in space_string:
        space_string = space_string.replace("  "," ")
    return space_string
        
print("Da li je uneseni simbol cifra?",da_li_je_cifra(simbol))
print("Da li je uneseni izraz palindrom?",da_li_je_palindrom(palindrom))
print("Slovo je promijenilo velicinu:",promijeni_velicinu(slovo))
print("Broj rijeci u recenici je:",broj_rijeci_u_stringu(recenica))
print("Najduza rijec u recenici je:",najduza_rijec_u_stringu(recenica))
print("Slovo koje se ponavlja je:",ista_slova(string))
print("Da li se drugi string nalazi u prvom?", substring(string1, string2))
print("String sa uklonjenim viskom blankova:", space(space_string))