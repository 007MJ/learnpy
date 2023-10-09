import random

def print_random_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    random_word = random.choice(words)
    for i in range(0, len(random_word)):
        print("#", end="")
    print()
    return random_word

def if_len_one(user):
    if len(user) > 1:
        return (-1)
    return (1)

def is_inWord(user, words):
    if user in words:
        return (1)
    return (-1)

def user_input():
    user = input("Enter a caracter : ")
    while (if_len_one(user) != 1):
        user = input("Enter a caracter : ")
    return (user)

def main():
    point = 0
    s = 0
    input("enter if you want to play :")
    words = print_random_word()
    save = "#" * len(words)
    for s in range(0, len(words)):
        letter = user_input()
        save = ""
        for i in words:
            if i == letter:
                save += i
                point += 1
            else :
                save += "#"
        print(save)
        print()
    if point == len(words):
        print("great 😁")
    else:
        print("you did not fund the word the word is", words)

main()

