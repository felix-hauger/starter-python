user_input = input("Rentrez le texte à écrire dans le fichier output.txt\n>")

file = open("output.txt", "a")

file.write(user_input + "\n")

file = open("output.txt", "r")

print(file.read())