upustvo = input("Unesite upustvo: ")

def pronadji_blago(upustvo):
    """
    Kapetan Flint je sakrio blago na tajanstvenom ostrvu, ali je ostavio opis kako ga naci. Opis se satoji od stringova oblika
    "North 5", gdje je rijec jedna od "North", "South", "East", "West" i daje pravac kretanja, a broj daje koliko koraka treba
    napraviti u datom smjeru. Pocetak se nalazi u koordinatnom pocetku, x osa je usmjerena ka East, a y osa ka North. 
    Na osnovu datog opisa returns koordinate blaga.
    """
    pocetakx = 0
    pocetaky = 0
    while upustvo != "kraj":
        upustvo = upustvo.split(" ")
        pravac = upustvo[0]
        koraci = int(upustvo[1])
        if pravac == "North":
            pocetaky = pocetaky + koraci
        elif pravac == "South":
            pocetaky = pocetaky - koraci
        elif pravac == "East":
            pocetakx = pocetakx + koraci
        elif pravac == "West":
            pocetakx = pocetakx - koraci
        upustvo = input("Unesite upustvo: ")
    return pocetakx, pocetaky
print(pronadji_blago(upustvo))
