import re

# Get data file in a string
data_string = open("data.txt").read()

# Convert it in a list matching only alphabet characters
words = re.findall("[a-zA-Z]+", data_string)

# Browse through the list with a loop to count number of words
words_count = 0

for word in words:
    words_count += 1

print(words_count)

# Un grand merci à Rodrigue pour m'avoir aidé avec les regexes !