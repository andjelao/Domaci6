"""
Jedno polje sahovske table opisuje se sa dva prirodna broja (a, b) ne veca od 8: a je redni broj horizontale (slijeva udesno),
b je redni broj vertikale (odozdo navise). Dati su prirodni brojevi a, b, c, d, e, f, svi manji od 9. Bijela figura je
postavljena na na (a,b), a crna na (c,d). Provjeriti moze li bijela figura doci na polje (e,f) a da ne bude napadnuta od
crne figure. Probati svaku kombinaciju figura (npr. dama i dama, dama i top, dama i lovac, dama i konj, lovac i dama, kralj
i konj)
"""
print("Sahovska tabla sa oznacenim pozcijama: x -> prva cifra, koji predstavlja red i druga cifra y -> predstavlja kolonu")
board = [["00","01","02","03","04","05","06","07"], ["10","11","12","13","14","15","16","17"], ["20","21","22","23","24","25","26","27"],["30","31","32","33","34","35","36","37"],
["40","41","42","43","44","45","46","47"], ["50","51","52","53","54","55","56","57"], ["60","61","62","63","64","65","66","67"], ["70","71","72","73","74","75","76","77"],]

#tabla koja sadrzi raspored bijelih i crnih polja
board_color = [["b","c","b","c","b","c","b","c"], ["c","b","c","b","c","b","c","b"], ["b","c","b","c","b","c","b","c"],["c","b","c","b","c","b","c","b"],
["b","c","b","c","b","c","b","c"], ["c","b","c","b","c","b","c","b"], ["b","c","b","c","b","c","b","c"], ["c","b","c","b","c","b","c","b"],]

def print_board():
    for i in range(len(board)):
        print(board[i])
print_board()
print("")

print("Unesite koordinate bijele figure: ")
a = int(input("redni broj horizontale: "))
b = int(input("redni broj vertikale: "))
print("Unesite koordinate crne figure: ")
c = int(input("redni broj horizontale: "))
d = int(input("redni broj vertikale: "))
print("Unesite koordinate polja na koje biste zeljeli da pomjerite bijelu figuru: ")
e = int(input("redni broj horizontale: "))
f = int(input("redni broj vertikale: "))
print("")

lista_bijelih = []
lista_crnih = []

def can_it_move(x, y, z, q):
    figure = ["kralj", "kraljica", "top", "lovac", "skakac"]
    lista_figura = ["kralj", "kraljica", "top", "lovac", "skakac"]
    for vrsta_figure in figure:
        if vrsta_figure == "kralj":
            if abs(z - x) <= 1 and abs(q - y) <= 1:
                pass
            else:
                lista_figura.remove("kralj")
        elif vrsta_figure == "kraljica":
            if x == z or y == q or abs(x - z) == abs(y -q):
                pass
            else:
                lista_figura.remove("kraljica")
        elif vrsta_figure == "top":
            if x == z or y == q:
                pass
            else:
                lista_figura.remove("top")
        elif vrsta_figure == "lovac":
            boja_polja = board_color[x][y]
            if abs(x - z) == abs(y -q) and board_color[z][q] == boja_polja:
               pass
            else:
                lista_figura.remove("lovac")
        elif vrsta_figure == "skakac":
            if abs(x -z) == 2 and abs(y - q) == 1:
                pass
            else:
                lista_figura.remove("skakac") 
    return lista_figura 

def bijeli_pjesak(x,y,z,q):
    #provjerava da li je bijeli pjesak na pocetnoj poziciji a to je sesti red table - ako jeste
    #on moze da se krece dva polja unaprijed
    if x == 6:
        if z - x == -2 and q - y == 0:
            lista_bijelih.append("pjesak")
        #ako nije pocetna pozicija
    elif z - x == -1 and q - y == 0:
        lista_bijelih.append("pjesak")
def crni_pjesak(x,y,z,q):
    #provjerava da li crni pjesak moze da pojede bijelu figuru na poziciji z, q
    #pjesaci mogu da pojedu figuru ako se pomjere jedno polje po dijagonali unaprijed
    if x - z == -1 and abs(y - q) == 1:
        lista_crnih.append("pjesak")

def sah(a, b, c, d, e, f):
    #print_board()
    global lista_bijelih
    lista_bijelih = can_it_move(a, b, e, f)
    bijeli_pjesak(a,b,e,f)
    global lista_crnih
    lista_crnih = can_it_move(c,d,e,f)
    crni_pjesak(c,d,e,f)

    for y in lista_crnih:
        for x in lista_bijelih:
            print(y,"ce napasti",x) 

sah(a, b, c, d, e, f)






