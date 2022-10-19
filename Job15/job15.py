def sayHello(firstname, lastname):
    # test if first name is empty
    if len(firstname) == 0:
        print("Entrez un prénom")
    # test if last name is empty, more test are possibles, for exemple the number and type of characters
    elif len(lastname) == 0:
        print("Entrez un nom de famille")
    else:
        # the brackets act as a placeholder for parameters
        print("Bonjour {} {}".format(firstname, lastname))

userinput_firstname = input("Quel est votre prénom ? > ")
userinput_lastname = input("Quel est votre nom de famille ? > ")

sayHello(firstname=userinput_firstname, lastname=userinput_lastname)