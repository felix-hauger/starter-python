myList = []

def add_to_list(*numbers):

    for number in numbers:
        if isinstance(number, int) or isinstance(number, float):
            myList.append(number)

    for list_number in myList:
        if list_number % 2 == 0:
            print(list_number)

add_to_list(7, 8, 1, 2, 14, 10.5, 124, 51)
