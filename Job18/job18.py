def sort_numbers(*numbers):

    myList = []
    
    for number in numbers:
        # using type() instead of isinstance() because the last interprets booleans as 1 and 0
        if type(number) is int or type(number) is float:
            myList.append(number)
    
    myList.sort()

    print(myList)

sort_numbers(7, 8, 1, 2, -19, 14, 0, 10.5, 124, 51, 10**2, "bonjour", True, False)