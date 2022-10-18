nb_hauteur = int(input("Entrez la hauteur de votre triangle >"))

base = "__" * int(nb_hauteur-1)
left_side = " " * nb_hauteur + "/"
right_side = ""

for x in range(0, nb_hauteur-1):
    left_side = left_side[1:]
    right_side = " " * x * 2 + "\\"
    print(left_side + right_side)

print("/" + base + "\\")