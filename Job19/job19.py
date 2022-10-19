
def sort_numbers(*numbers):

    myList = []
    mySortedList = myList
    numberSortedIndexDict = {}

    for number in numbers:
        # using type() instead of isinstance() because the last interprets booleans as 1 and 0
        if type(number) is int or type(number) is float:
            myList.append(number)
    print(myList)


    # ADD SORT FUNCTION HERE
    for list_number in myList:

        # get
        number_sorted_index = 0

        for list_nb in myList:
            if list_number > list_nb:
                number_sorted_index += 1
        numberSortedIndexDict[list_number] = number_sorted_index

        print(numberSortedIndexDict)
        
            # mySortedList.insert(numberSortedIndexDict[list_number], list_number)

        print(myList)
        # print(mySortedList)
        
        # myList.insert(numberSortedIndexDict[list_number], myList.pop(myList.index(list_number)))

        

        print('index de {} : {}'.format(list_number, numberSortedIndexDict[list_number]))


    # for list_number in myList:
    #     myList.insert(numberSortedIndexDict[list_number], myList.pop(myList.index(list_number)))
    #     # mySortedList.insert(numberSortedIndexDict[list_number], list_number)
    #     print(mySortedList)

    print('')
    print(numberSortedIndexDict)
    # print(myList)
    # print(mySortedList)

sort_numbers(7, 8, 1, 2, -19, 14, 0, 10.5, 124, 51, 10**2, "bonjour", True, False)
