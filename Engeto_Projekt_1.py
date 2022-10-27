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
chosen_text = text.split()
word_list = []
words_lenghts = []

word_count = 0
word_title = 0
word_uppercase = 0
word_lowercase = 0
word_isnumeric = 0
sum_all_num = 0

for word in chosen_text:
    word = word.strip(',.')
    word_list.append(word)

for word in word_list:
    word_count += 1
    words_lenghts.append(len(word))

    if word.istitle():
        word_title += 1
    elif word.isupper():
        word_uppercase += 1
    elif word.islower():
        word_lowercase += 1
    elif word.isnumeric():
        word_isnumeric += 1
        sum_all_num += int(word)

print(
    f'There are {word_count} words in the selected text.',
    f'There are {word_title} titlecase words.',
    f'There are {word_uppercase} uppercase words.',
    f'There are {word_lowercase} lowercase words.',
    f'There are {word_isnumeric} numeric strings.',
    f'The sum of all numbers {sum_all_num}',
    line,
    f'LEN|   OCCURENCES   |NR.',
    line,
    f'  1|{"*" * words_lenghts.count(1)}|{words_lenghts.count(1)}',
    f'  2|{"*" * words_lenghts.count(2)}|{words_lenghts.count(2)}',
    f'  3|{"*" * words_lenghts.count(3)}|{words_lenghts.count(3)}',
    f'  4|{"*" * words_lenghts.count(4)}|{words_lenghts.count(4)}',
    f'  5|{"*" * words_lenghts.count(5)}|{words_lenghts.count(5)}',
    f'  6|{"*" * words_lenghts.count(6)}|{words_lenghts.count(6)}',
    f'  7|{"*" * words_lenghts.count(7)}|{words_lenghts.count(7)}',
    f'  8|{"*" * words_lenghts.count(8)}|{words_lenghts.count(8)}',
    f'  9|{"*" * words_lenghts.count(9)}|{words_lenghts.count(9)}',
    f' 10|{"*" * words_lenghts.count(10)}|{words_lenghts.count(10)}',
    f' 11|{"*" * words_lenghts.count(11)}|{words_lenghts.count(11)}',
    f' 12|{"*" * words_lenghts.count(12)}|{words_lenghts.count(12)}',
    f' 13|{"*" * words_lenghts.count(13)}|{words_lenghts.count(13)}',
    line,
    sep='\n'
    )

print(words_lenghts)



