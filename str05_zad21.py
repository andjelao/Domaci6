ulaz = input("Unesite broj galeona, srpova i knutova odvojeni razmakom: ")

def novac_izrazen_u_knutovima(ulaz):
    """
    ulazni parametar: string unos koji sadrzi brojeve galeona, srpova i knutova odvojene razmacima
    returns unesenu kolicinu nova izrazenu u knutovima
    """
    ulaz = ulaz.split()
    galeoni = int(ulaz[0])
    srpovi = int(ulaz[1])
    knutovi = int(ulaz[2])
     
    return knutovi + srpovi * 29 + galeoni * 17 * 29
    

print(novac_izrazen_u_knutovima(ulaz))
