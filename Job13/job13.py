import re

nb_characters = int(input("Quelle taille pour vos mots ? > "))

data_string = open("data.txt").read()

words = re.findall("[a-zA-Z]+", data_string)

words_count = 0

# count the words in the list, then the characters in the word
for word in words:
    # reset the character count to 0
    char_count = 0
    # count the characters
    for char in word:
        char_count += 1
    # test if the number of characters of the word match the given number, if so add +1 to the words_count variable
    if char_count == nb_characters:
        words_count += 1
        

print(words_count)