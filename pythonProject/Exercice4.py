# nombre = int(input("Entrez un nombre : "))
# while nombre < 1 :
#    nombre = int(input("Erreur, entrez un nombre positif : "))
#
# n=nombre
# print("Voici tous les nombres en sens inverse à partir de", nombre," : ")
# while n > 0:
#     print(n, end=" ")
#     n -=1

num = int(input("Entrer le nombre: "))
print("LE nombre inverse est: ")
for i in range(num, 0, -1):
    print(i, end=" ")