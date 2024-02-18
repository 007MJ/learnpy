import random 

list_word = [ "ACTEUR ","AVIRON", "BOXEUR", "BRONZE", "BUDGET", "CARTON", "CHAQUE", "CHEVAL" ]

one_word = random.choice(list_word)
while len(one_word) != 6 :
    one_word = random.choice(list_word)


print("Trouve un mo qui a la longuer ", len(one_word))

for tour in range(8):
    usr = input("Entre un mot : ")
    if len(usr)  != len(one_word):
        print("......... longuer de votre mot est ", len(usr))
    else:
        for i in range(len(one_word)):
            usr_letter = usr[i]
            random_letter = one_word[i]
            if usr_letter.upper() == random_letter:
                print(usr_letter.upper() + "#", end = '')
            else:
                if one_word.find(usr_letter) >= 0 :
                    print(usr_letter.upper() + "?", end=" ")
                else:
                    lower = usr_letter.lower()
                    print(str(lower) + " ", end = ' ')
        print()
        if usr.upper() == one_word:
            print('WIN 🎇')
            exit()
        

print("le mot etait ", one_word)