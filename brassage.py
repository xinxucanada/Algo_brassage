type=['♦','♣','♥','♠']
carteNb=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
carteListe=[]
for i in type:
    for j in carteNb:
        carteListe.append(j+i)
# print(carteListe)
def affichage(cartes):
    for i in range(4):
        for j in range(13):
            print(cartes[i*13+j],end="\t")
        print()
def brasseCartes(cartes):
    paquet1=cartes[:26]
    paquet2=cartes[26:]
    newCarteliste=[]
    for i in range(26):
        newCarteliste.append(paquet1[i])
        newCarteliste.append(paquet2[i])
    cartes=newCarteliste
    return cartes
def sauvegard(cartes):
    f=open("cards.txt","w",encoding="utf-8")
    for i in range(4):
        for j in range(13):
            f.write(cartes[i*13+j]+"\t")
        f.write("\n")

def opptions():
    print('Choisissez les options suivantes: ')
    print(
        "1. l'état du jeu de carte\n2. Effectuer un brassage inter-coupé\n3. Sauvegarder l'état final dans un fichier .txt\n")
    option = input("Choisissez: ")
    return option

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