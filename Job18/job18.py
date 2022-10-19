myList = []

def sort_numbers(*numbers):

    for number in numbers:
        # using type instead() of isinstance() because the last accepts booleans
        if type(number) is int or type(number) is float:
            myList.append(number)
    
    myList.sort()

    print(myList)

sort_numbers(7, 1, 100000, 95.5, -19, 10**2)