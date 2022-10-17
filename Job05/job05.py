
input1 = int(input("Entrez votre première valeur\n>"))
input2 = int(input("Entrez votre seconde valeur\n>"))

print("Valeur 1 : " + str(input1))
print("Valeur 2 : " + str(input2))

if input1 < input2:
    for x in range(input1+1, input2):
        print(x)
elif input1 > input2:
    for x in range(input1-1, input2, -1):
        print(x)
elif input1 == input2:
    print("Valeurs égales")