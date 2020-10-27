lozinka = input("Unesite Vasu lozinku: ")

def da_li_je_jaka_lozinka(lozinka):
    """
    ulazni parametar: string lozinka
    returns boolean da li je lozinka jaka: - ako sadrzi najmanje 8 karaktera
                                           - ako sadrzi mala slova, velika slova i cifre 
    """
    malo_slovo = False
    veliko_slovo = False
    broj = False
    if len(lozinka) >= 8:
        for x in lozinka:
            if x.islower():
                malo_slovo = True
            if x.isupper():
                veliko_slovo = True
            if x.isdigit():
                broj = True      
        return malo_slovo and veliko_slovo and broj
    else: 
        return False
print(da_li_je_jaka_lozinka(lozinka))