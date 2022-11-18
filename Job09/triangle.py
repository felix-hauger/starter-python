nb_hauteur = int(input("Entrez la hauteur de votre triangle >"))

base = "__" * int(nb_hauteur-1)
left_side = " " * nb_hauteur + "/"
right_side = "\\"

for x in range(nb_hauteur-1):
    # à chaque tour de boucle left_side est égal à left_side à partir de l'index 1, ce qui va réduire sa taille au bon endroit
    left_side = left_side[1:]
    right_side = " " * x * 2 + "\\"
    print(left_side + right_side)

print("/" + base + "\\")