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
        "é" : "É",
        "è" : "È",
        "ê" : "Ê",
        "ë" : "Ë",
        "à" : "À",
        "ç" : "Ç",
        "î" : "Î",
        "ï" : "Ï",
        "ù" : "Ù",
        "û" : "Û",
        "ü" : "Ü",
        "ô" : "Ô"
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

def myLower(myString:str):
    string_list = list(myString)
    up_to_low = {
        "A" : "a",
        "B" : "b",
        "C" : "c",
        "D" : "d",
        "E" : "e",
        "F" : "f",
        "G" : "g",
        "H" : "h",
        "I" : "i",
        "J" : "j",
        "K" : "k",
        "L" : "l",
        "M" : "m",
        "N" : "n",
        "O" : "o",
        "P" : "p",
        "Q" : "q",
        "R" : "r",
        "S" : "s",
        "T" : "t",
        "U" : "u",
        "V" : "v",
        "W" : "w",
        "X" : "x",
        "Y" : "y",
        "Z" : "z",
        "É" : "é",
        "È" : "è",
        "Ê" : "ê",
        "Ë" : "ë",
        "À" : "à",
        "Ç" : "ç",
        "Î" : "î",
        "Ï" : "ï",
        "Ù" : "ù",
        "Û" : "û",
        "Ü" : "ü",
        "Ô" : "ô"
    }

    # x used for string_list handling by index
    x = 0
    for char in string_list:
        # if char is in the keys of up_to_low, replace the current character by the value of the key of the dictionnary
        if char in up_to_low:
            string_list[x] = up_to_low[char]
        x += 1
            
    lower_string = ""
    for char in string_list:
        lower_string += char

    return lower_string


print(myLower("HEY"))

# def myTitle():



# def myClean():


