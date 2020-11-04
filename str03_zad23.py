x = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))
def zamjena_vrijednosti(x, y):
    """
    ulazni parametri: promjenjive x i y
    mijenja mjesta vrijednostima x i y
    """
    x, y = y, x
    print(x, y)

zamjena_vrijednosti(x, y)
