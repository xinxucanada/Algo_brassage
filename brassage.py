



def affichage(cartes):
    for i in range(4):
        for j in range(13):
            print(cartes[i*13+j],end="\t")
        print()
#Dans ce cas-ci, 26 fonctionne mais idéalement trouve la valeur de manière dynamique (len(cartes)//2)
def brasseCartes(cartes):
    paquet1=cartes[:len(cartes)//2]
    paquet2=cartes[len(cartes)//2:]
    newCarteliste=[]
    for i in range(len(cartes)//2):
        newCarteliste.append(paquet1[i])
        newCarteliste.append(paquet2[i])
    cartes=newCarteliste
    return cartes
#Bonne approche pour séparer le paquet en 4 lignes. Ici aussi tu pourrais dynamiquement trouvé 13=len(cartes)//4 pour avoir 4 lignes de longueur égale.
def sauvegard(cartes):
    f=open("cards.txt","w",encoding="utf-8")
    for i in range(4):
        for j in range(len(cartes)//4):
            f.write(cartes[i*13+j]+"\t")
        f.write("\n")
    f.close()

#C'est excellent de mettre ton menu dans une fonction, mais tu devrais aussi y mettre ton while
def opptions():
    print('Choisissez les options suivantes: ')
    print(
        "1. l'état du jeu de carte\n2. Effectuer un brassage inter-coupé\n3. Sauvegarder l'état final dans un fichier .txt\n")
    option = input("Choisissez: ")
    return option

#Évite d'écrire du code d'exécution normale(indentation de gauche) avant tes définitions de fonction
#Bonne utilisation de tableaux pour générer ton paquet.

type=['♦','♣','♥','♠']
carteNb=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
carteListe=[]

for i in type:
    for j in carteNb:
        carteListe.append(j+i)
ans=opptions()

while ans!="4" and ans!="3":

    if ans=="1":
        affichage(carteListe)
        ans=opptions()

    elif ans=="2":
        carteListe = brasseCartes(carteListe)
        ans = opptions()
    else:
        print("Veuillez choisir entre 1 a 4")
        ans = opptions()
if ans=="3":
    sauvegard(carteListe)

print("Au-revoir")