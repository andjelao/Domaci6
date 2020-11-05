a = float(input("Unesite broj a: "))
#zajednicka promjenjiva za sve primjere
a1 = a * a
#zajednicka promjeinjiva za a, b, c i d primjere
a2 = a1 * a1
def primjer_a(a, a1, a2):
    """
    ulazni parametar : realan broj a koji unosi korisnik, promjenjive a1 i a2
    returns a^7 izracunat samo pomocu 4 operacije mnozenja i pomocnih promjenjivih
    """
    return a2 * a1 * a
def primjer_b(a, a1, a2):
    """
    ulazni parametar : realan broj a koji unosi korisnik, promjenjive a1 i a2
    returns a^10 izracunat samo pomocu 4 operacije mnozenja i pomocnih promjenjivih
    """
    return a2 * a2 * a1
def primjer_c(a, a1, a2):
    """
    ulazni parametar : realan broj a koji unosi korisnik, promjenjive a1 i a2
    returns a^21 izracunat samo pomocu 6 operacija mnozenja i pomocnih promjenjivih
    """
    a3 = a2 * a2 * a1
    return a3 * a3 * a
def primjer_d(a, a1, a2):
    """
    ulazni parametar : realan broj a koji unosi korisnik, promjenjive a1 i a2
    returns a^64 izracunat samo pomocu 6 operacija mnozenja i pomocnih promjenjivih
    """
    a3 = a2 * a2
    a4 = a3 * a3
    a5 = a4 * a4
    return a5 * a5
def primjer_e(a, a1):
    """
    ulazni parametar : realan broj a koji unosi korisnik, promjenjiva a1
    returns a^3 i a^10  izracunat samo pomocu 4 operacije mnozenja i pomocnih promjenjivih
    """
    a2 = a1 * a
    a3 = a2 * a1
    a4 = a3 * a3
    return a2, a4
def primjer_f(a, a1):
    """
    ulazni parametar : realan broj a koji unosi korisnik, promjenjiva a1
    returns a^2, a^5 i a^17  izracunat samo pomocu 6 operacija mnozenja i pomocnih promjenjivih
    """
    a2 = a1 * a1 * a
    a3 = a2 * a2 * a2 * a1
    return a1, a2, a3
print(primjer_a(a, a1, a2))
print(primjer_b(a, a1, a2))
print(primjer_c(a, a1, a2))
print(primjer_d(a, a1, a2))
print(primjer_e(a, a1))
print(primjer_f(a, a1))