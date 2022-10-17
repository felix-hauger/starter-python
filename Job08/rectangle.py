nb_largeur = int(input("Entrez la largeur de votre rectangle >"))
nb_hauteur = int(input("Entrez la hauteur de votre rectangle >"))

if nb_largeur < 1 or nb_hauteur < 1:
    print("Entrez des nombres entiers positifs.")
    
else:
    largeur = ""
    hauteur = ""
    remplissage = ""

    for x in range(0, nb_largeur):
        largeur += "-"
        remplissage += " "

    print("|" + largeur + "|")

    # enlevé 2 pour la bordure du haut et du bas
    for x in range(0, nb_hauteur-2):
        print("|" + remplissage + "|")

    print("|" + largeur + "|")

