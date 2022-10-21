def myUpper(myString:str):
    string_list = list(myString)
    low_to_up = {
        "a" : "A",
        "b" : "B",
        "c" : "C",
        "d" : "D",
        "e" : "E",
        "f" : "F",
        "g" : "G",
        "h" : "H",
        "i" : "I",
        "j" : "J",
        "k" : "K",
        "l" : "L",
        "m" : "M",
        "n" : "N",
        "o" : "O",
        "p" : "P",
        "q" : "Q",
        "r" : "R",
        "s" : "S",
        "t" : "T",
        "u" : "U",
        "v" : "V",
        "w" : "W",
        "x" : "X",
        "y" : "Y",
        "z" : "Z",
    }

    # x used for string_list handling by index
    x = 0
    for char in string_list:
        # if char is in the keys of low_to_up, replace the current character by the value of the key of the dictionnary
        if char in low_to_up:
            string_list[x] = low_to_up[char]
        x += 1
            
    upper_string = ""
    for char in string_list:
        upper_string += char

    return upper_string


print(myUpper("hellothere"))

# def myLower():



# def myTitle():



# def myClean():


