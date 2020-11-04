
print("Unesite koordinate tacke A: ")
a1 = int(input("x: "))
a2 = int(input("y: "))
print("Unesite koordinate tacke B: ")
b1 = int(input("x: "))
b2 = int(input("y: "))
print("Unesite koordinate tacke C: ")
c1 = int(input("x: "))
c2 = int(input("y: "))
print("Unesite koordinate tacke za provjeru: " )
x = int(input("x: "))
y = int(input("y: "))

def da_li_tacka_pripada_trouglu(a1, a2, b1, b2, c1, c2, x, y):
    """
    ulazni parametri: koordinate tacaka trougla -> A(a1, a2), B(b1, b2), C(c1, c2) i tacke koju provjeravamo P(x,y)
    tacka pripada trouglu ako je povrsina trougla ABC jednaka zbiru trouglova koje tacka P formira sa tackama trougla ABC
    returns boolean ako tacka pripada trouglu, ukljucujuci njegove stranice
    """
    povrsina_abc = (abs(a1 * (b2 - c2) + b1 * (c2 - a2) + c1 * (a2 - b2))) / 2
    if povrsina_abc == 0:
        print("Trougao ne postoji!")
    else:
        povrsina_abp = (abs(a1 * (b2 - y) + b1 * (y - a2) + x * (a2 - b2))) / 2
        povrsina_apc = (abs(a1 * (y - c2) + x * (c2 - a2) + c1 * (a2 - y))) / 2
        povrsina_bcp = (abs(b1 * (c2 - y) + c1 * (y - b2) + x * (b2 - c2))) / 2
        return povrsina_abc == povrsina_abp + povrsina_apc + povrsina_bcp
print(da_li_tacka_pripada_trouglu(a1, a2, b1, b2, c1, c2, x, y))