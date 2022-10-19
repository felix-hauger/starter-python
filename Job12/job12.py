import re

# Get data file in a string
data_string = open("data.txt").read()

# Convert it in a list matching only alphabet characters
words = re.findall("[a-zA-Z]+", data_string)

# Browse through the list with a loop to count number of words
nb_words = 0

for word in words:
    nb_words+=1

print(nb_words)