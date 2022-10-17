from operator import truediv


while True:
    userinput = input(">")
    if userinput == "Bonjour":
        print("Bonjour à toi")
    elif userinput == "Au revoir":
        break
    else:
        print(userinput)