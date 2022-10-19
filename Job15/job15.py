def sayHello(firstname, lastname):
    print("Bonjour {} {}".format(firstname, lastname))

userinput_firstname = input("Quel est votre prénom ? > ")
userinput_lastname = input("Quel est votre nom de famille ? > ")

sayHello(firstname=userinput_firstname, lastname=userinput_lastname)