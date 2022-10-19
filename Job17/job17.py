def add_to_list(*numbers):
    
    myList = []

    for number in numbers:
        # using type() instead of isinstance() because the last interprets booleans as 1 and 0
        if type(number) is int or type(number) is float:
            myList.append(number)

    # check if number is divisible by 2
    for list_number in myList:
        if list_number % 2 == 0:
            print(list_number)


add_to_list(7, 8, 1, 2, -19, 14, 0, 10.5, 124, 51, 10**2, "bonjour", True, False)

