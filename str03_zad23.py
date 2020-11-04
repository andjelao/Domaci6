x = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))
print("Prije: ",x,y)
def zamjena_vrijednosti(x, y):
    """
    ulazni parametri: promjenjive x i y
    mijenja mjesta vrijednostima x i y
    """
    temp = x
    x = y
    y = temp
    print("Poslije",x, y)

zamjena_vrijednosti(x, y)
