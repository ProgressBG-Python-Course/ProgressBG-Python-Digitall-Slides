# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here
def solution1(n):
    for i in range(1, n+1):
        print( '*' * i )

### EXPECTED OUTPUT:
# Enter stars number: 4
# *
# **
# ***
# ****


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a script that prompts the user to enter words, one at a time.
    The user should continue to enter words until they enter '0'.
    After the user enters '0', the script should display all the words that start with a vowel (a, e, i, o, u).
"""

### Your code

def solution2():
    words = []
    word = input("Enter a word (or '0' to stop): ")

    while word != '0':
        words.append(word)
        word = input("Enter a word (or '0' to stop): ")

    vowels = 'aeiou'
    words_started_with_vowels = [word for word in words if word[0].lower() in vowels]

    print("Words that start with a vowel:", words_started_with_vowels)


### EXPECTED OUTPUT:
# Enter a word (or '0' to stop): atom
# Enter a word (or '0' to stop): see
# Enter a word (or '0' to stop): end
# Enter a word (or '0' to stop): 0
# Words that start with a vowel: ['atom', 'end']


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a function that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
words = ["hello", "world", "python", "is", "fun", "and", "useful"]

### Your code here
def solution3(strings):
    length_dict = {}
    for s in strings:
        length = len(s)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(s)
    print(length_dict)
# solution3(words)

### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['useful']}



# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    In a supermarket inventory system, there are two sets of product categories:
    1. Categories that need refrigeration.
    2. Categories on sale this week.

    Write a script, which performs the following tasks:
    a. Find and print the categories that are both refrigerated and on sale.
    b. Find and print categories that are on sale but do not require refrigeration.
    c. Suggest new sale categories from the refrigerated items which are not yet on sale.

    Note: The category names are assumed to be in lowercase.
"""

### Hardcoded sets
refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

def solution4():
    # a. Categories both refrigerated and on sale
    refrigerated_and_sale = refrigerated.intersection(sale)
    print("Categories both refrigerated and on sale:", refrigerated_and_sale)

    # b. Categories on sale but not refrigerated
    sale_not_refrigerated = sale.difference(refrigerated)
    print("Sale categories not needing refrigeration:", sale_not_refrigerated)

    # c. Suggesting new sale categories from refrigerated items not yet on sale
    new_sale_suggestions = refrigerated.difference(sale)
    print("Suggested new sale categories from refrigerated items:", new_sale_suggestions)

solution4()

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}