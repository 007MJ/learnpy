def trythe(old):
    try:
        int_old = int(old)
    except:
        print("You need to enter a number")
        return (-1)
    return (int_old)

def is_major(age):
    if age > 18:
        print("your are major")
    else:
        print("your are minor")

old = input("old : ")
age = trythe(old)
if age != -1:
    is_major(age)



