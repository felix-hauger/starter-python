nb_hauteur = int(input("Entrez la hauteur de votre triangle >"))

base = ""
left_side = "/"
right_side = ""

for x in range(1, nb_hauteur):
    base += "__"

left_side = " " * nb_hauteur + left_side

for x in range(0, nb_hauteur-1):
    left_side = left_side[1:]
    right_side = " " * x * 2 + "\\"
    print(left_side + right_side)

print("/" + base + "\\")