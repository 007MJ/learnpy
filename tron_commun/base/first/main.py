def printinfo(age, n, name, taille = 1.75):
    if n == 1:
        print(f"How are you doing {name} ohh you will get  {age} in one year and your {taille} m")
        if age == 17:
            print("you are almost an adult")
        elif age == 18:
            print("you are just an adult")
        elif age > 60 :
            print("You are an senoir")
        elif age > 18:
            print("you are just an adult")
        elif age < 10 :
            print("you are kid")
        else:
            print("you are minor")
            
    else:
        print("you need to enter number or the name is empty")


age = 0

name = ""

while age == 0 or name == "":
    try:
        name = input("what is your name : ")
        age = int(input("what is your age : "))
    except:
        printinfo(age, 0, name)



age +=1
printinfo(age, 1, name, 2)