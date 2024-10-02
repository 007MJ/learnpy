import random

min_nb = 1
max_nb = 10
magic_nb = random.randint(min_nb, max_nb)

def ask_number(nb1, nb2):
    nb_str = ""
    while nb_str == "" :
        nb_str = input(f"what is the magic number between {nb1} and {nb2} :")
        try:
            nb_int = int(nb_str)
        except:
            nb_str = ""
            print("enter an number ")
        else :
             if nb_int > max_nb or nb_int < min_nb:
                print("number must be between {max_nb} and {min_nb}")
                nb_str = ""
    return nb_int

input_nb = magic_nb + 1
life = 3
for i in range(0, life):
    input_nb  = ask_number(min_nb, max_nb)
    life -= 1
    if input_nb == magic_nb:
        break;


if life == 0:
    print(f"you have lose the magic is {magic_nb}")
else:
    if input_nb == magic_nb:
            print("You have gusse the number")
    elif input_nb > magic_nb:
        print("Your number is beggier")
    else:
        print("Your number is lower")