""" 
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Boček
email: michal.678@seznam.cz
discord: Michal B.#2426 
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
texts_count = len(TEXTS)
line = 40 * "-"

logins = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

username = input("Username: ")
password = input("Password: ")

if logins.get(username) == password:
    print(line)
    print("Welcome to the app,", username)
    print("We have", texts_count, "texts to be analyzed.")
    print(line)
    
else:
    print("Unregistered user, terminating program...")
    exit()

selection = int(input(f"Enter a number btw. 1 and {texts_count} to select: "))
print(line)

if selection > len(TEXTS):
    print("Invalid seletion. Terminating...")
    exit()

text = TEXTS[selection - 1]
text_pure = text.replace(",", " ").replace(".", " ").replace("\n", " ").split()

word_count = 0
word_title = 0
word_uppercase = 0
word_lowercase = 0
word_isnumeric = 0
sum_all_num = 0

letters_1 = 0
letters_2 = 0
letters_3 = 0
letters_4 = 0
letters_5 = 0
letters_6 = 0
letters_7 = 0
letters_8 = 0
letters_9 = 0
letters_10 = 0
letters_11 = 0
letters_12 = 0
letters_13 = 0
letters_14 = 0
letters_15 = 0

for word in text_pure:
    if word.isalpha():
        word_count += 1
    if word.istitle():
        word_title += 1
    if word.isupper() and word.isalpha():
        word_uppercase += 1
    if word.islower() and word.isalpha():
        word_lowercase += 1
    if word.isdigit():
        word_isnumeric += 1
        sum_all_num += int(word)
    if len(word) == 1:
        letters_1 += 1
    if len(word) == 2:
        letters_2 += 1
    if len(word) == 3:
        letters_3 += 1
    if len(word) == 4:
        letters_4 += 1
    if len(word) == 5:
        letters_5 += 1
    if len(word) == 6:
        letters_6 += 1
    if len(word) == 7:
        letters_7 += 1
    if len(word) == 8:
        letters_8 += 1
    if len(word) == 9:
        letters_9 += 1
    if len(word) == 10:
        letters_10 += 1
    if len(word) == 11:
        letters_11 += 1
    if len(word) == 12:
        letters_12 += 1
    if len(word) == 13:
        letters_13 += 1
    if len(word) == 14:
        letters_14 += 1
    if len(word) == 15:
        letters_15 += 1
    

print(line)
print(f"There are {word_count} words in the selected text.")
print(f"There are {word_title} titlecase words.")
print(f"There are {word_uppercase} uppercase words.")
print(f"There are {word_lowercase} lowercase words.")
print(f"There are {word_isnumeric} numeric strings.")
print(f"The sum of all numbers {sum_all_num}")
print(line)
print("LEN|OCCURENCES|NR.")
print(line)
print("1|", "*" * letters_1, "|", + letters_1) 
print("2|", "*" * letters_2, "|", + letters_2) 
print("3|", "*" * letters_3, "|", + letters_3) 
print("4|", "*" * letters_4, "|", + letters_4) 
print("5|", "*" * letters_5, "|", + letters_5) 
print("6|", "*" * letters_6, "|", + letters_6) 
print("7|", "*" * letters_7, "|", + letters_7) 
print("8|", "*" * letters_8, "|", + letters_8) 
print("9|", "*" * letters_9, "|", + letters_9) 
print("10|", "*" * letters_10, "|", + letters_10) 
print("11|", "*" * letters_11, "|", + letters_11) 
print("12|", "*" * letters_12, "|", + letters_12) 
print("13|", "*" * letters_13, "|", + letters_13) 
print("14|", "*" * letters_14, "|", + letters_14) 
print("15|", "*" * letters_15, "|", + letters_15)  



