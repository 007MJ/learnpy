def rev_print(str):
    l = len(str) - 1
    while (l >= 0):
        print(str[l], end='')
        l -=1


rev_print("bonjour")