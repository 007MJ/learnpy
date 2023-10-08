import random

def print_random_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    random_word = random.choice(words)

    for i in range(0, len(random_word)):
        print("#", end="")

def if_len_one(user):
    if len(user) > 1:
        return (-1)
    return (1)

def is_inWord(user, words):
    if user in words:
        return (1)
    return (-1)

def user_input():
    input("enter if you want to play :")
    user = input("Enter a caracter : ")
    while (if_len_one(user) != 1):
        user = input("Enter a caracter : ")
    return (user)

def print_dote():
    if is_inWord(user_input(), random_word()) == 1:
        

print(user_input())

