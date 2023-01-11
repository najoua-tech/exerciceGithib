# nb = int(input("Entrez un nombre  : "))
# while nb < 1:
#     nb = int(input("Saisie invalide, entrer un nombre positif"))
#
# print(f"Les nombres pairs avec pas de 2 à partir de 2 a {nb} sont : ")
# for i in range(2, nb +1, 2):
#     print(i, end="  ")

nombre=int(input("Entrer un nombre: "))
if nombre <= 0:
    print("Erreur, entrez un nombre positif")
else:
    print("Tous les nombres pairs à partir de ",nombre)
    for i in range(1, nombre + 1):
        if i % 2 == 1:
            continue
        print(i, end=" ")
