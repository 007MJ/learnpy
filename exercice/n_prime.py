
def is_prime(n):
    i = 2
    if n <= 1:
        return (0)
    while (i < n):
        if (n % i == 0):
            return (0)
        i += 1
    return (1)

somme = 0
int_s = input("Enter a integer : ")
for i in range (2 , int(int_s)):
    if is_prime(i) == 1:
        somme += i
print("somme all number to n enter", somme)
# n = 0
# for i in range(1, int(n)):
