
def sort_numbers(*numbers):

    myNumberList = []

    for number in numbers:
        # using type() instead of isinstance() because the last interprets booleans as 1 and 0
        if type(number) is int or type(number) is float:
            myNumberList.append(number)
    print(myNumberList)    


    for x in range(len(myNumberList)):
        for y in range(len(myNumberList)):
            if myNumberList[x] < myNumberList[y]:
                myNumberList[x], myNumberList[y] = myNumberList[y], myNumberList[x]

    print(myNumberList)    




sort_numbers(7, 8, 1, 2, -19, 14, 0, 10.5, 124, 51, 10**2, "bonjour", True, False, 12-5)
