def digit_number(str):
    for i in str:
        if i != '*' or i != '+' or i != '-' or i != '/':
            if (i.isalpha() == True):
                print("digit and signe only")
                return ""
    return str


def juste_number(str):
    _is_nb = False
    for index in range(len(str)-1):
        if str[index].isdigit():
            index += 1
            while str[index].isspace() and index < len(str)-1:
                _is_nb = True
                index += 1
            if _is_nb == True:
                if str[index].isdigit():
                    print("no operator")
                    return ""
            _is_nb = False
    return (str)

def signe(str):
    _signe = False
    for i in range(len(str) -1):
        _signe = False
        if str[i] == '*' or  str[i] == '-' or str[i] == '+' or str[i] == '/':
            if i > len(str) -1:
                if (str[i - 1].isspace()) == False:
                    print("space bewteen *")
                    return ""
            while (str[i].isspace()) == False and i < len(str) -1:
                    if (str[i] == '*' or  str[i] == '-' or str[i] == '+' or str[i] == '/') and _signe == False:
                        _signe = True
                    else:
                        print("To many signe")
                        return ""
                    i +=1

            _signe = False
            if i < len(str) -1:
                if (str[i + 1].isdigit()) == False:
                    print("is number", str[i])
                    print("Bad use of signe")
                    return ""
    return str
        

def take_number():
    str = ""
    while str == "":
        str = input("Enter :")
        if len(str) == 1:
            if str[0].isdigit() :
                return (str)
            else:
                str = ""
                continue
        str = juste_number(str)
        str = digit_number(str)
        str = signe(str)
        for index in range (len(str) - 1):
            if str[index].isdigit():
                if index < len(str):
                    if (str[index + 1].isdigit() == False) and (str[index + 1].isspace()) == False:
                        str = ""
                        print("Space bewteen signe and number")
                        break;


    return (str);  




usr_numbers = take_number()

