# Library Imports

import pandas as pd

# Lists

green_possible = set()  # Set of all possible values according to the green characters
yellow_possible = set()  # Set of all possible values according to the yellow characters
black_possible = set()  # Set of all possible values according to the black characters
possible = set()   # Set of all possible values
green_indices = []  # List of the indices which are green
black_indices = []  # List of the indices which are black
yellow_indices = []  # List of the indices which are yellow
green_letters = set()  # Set of the letters that are green
black_letters = set()  # Set of the letters that are black

# Receive input from user.

word = input("Word: ")
status = input("Colors (g=green, y=yellow, b=black): ")

# Compile all possible five-letter words into a pandas DataFrame, then convert it to an array.

data5 = pd.DataFrame.transpose(pd.read_csv("list.txt", sep=" "))
arr = data5.index.values

# Compile the indices of the green letters.

for i in range(0, 5):
    if status[i] == "g":
        green_indices.append(i)
        green_letters.add(word[i])

# Compile the indices of the black letters.

for i in range(0, 5):
    if status[i] == "b":
        black_indices.append(i)
        black_letters.add(word[i])

# Compile the indices of the yellow letters.

for i in range(0, 5):
    if status[i] == "y":
        yellow_indices.append(i)

# Parse all possible 5-letter words.

for str in arr:

    # Parse each character in each 5-letter word.

    for i in range(0, 4):
        intersect = black_letters.intersection(green_letters)
        green_tangible = True
        yellow_tangible = True
        black_tangible = True
        char = word[i]
        str_char = str[i]
        current_status = status[i]

        for j in black_indices:
            if word[j] in str and word[j] in intersect:
                black_tangible = False

        if black_tangible:
            black_possible.add(str)

        for j in green_indices:
            if word[j] != str[j]:
                green_tangible = False

        if green_tangible:
            green_possible.add(str)

        for j in yellow_indices:
            if not word[j] in str or j == str.index(word[j]):
                yellow_tangible = False

        if yellow_tangible:
            yellow_possible.add(str)

        possible = black_possible.intersection(green_possible).intersection(yellow_possible)

for str in possible:
    print(str)

