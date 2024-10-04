def multi(nb1, nb2) :
    return (nb1 * nb1)

def addition(nb1, nb2) :
    return (nb1 + nb1)

def soustraction(nb1, nb2) :
    return (nb1 - nb1)


def divisio(nb1, nb2) :
    return (nb1 / nb1)


def take_number():
    str = ""
    while str == "":
        str = input("Enter :")
        for i in str:
            if i == 32 or i.isdigit():
                return str
            else:
                str = ""
                print("NUmbers  and operators * / + -")
                break;

    return (str);  


usr_numbers = take_number()

