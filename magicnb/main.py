import random

min = 0
max = 10

def ask_number():
	nb_usr = 0
	while nb_usr == 0:
		try :
			usr = input("Entre un nombre : ")
			nb_usr = int(usr)
		except :
			print("Entre un nombre")
		else :
			return nb_usr

rand_nb = random.randint(min, max)
nb_try = 4

print(f"Le nombre d'essai {nb_try}")
print(f"Un nombre entre ( {min} et {max} )")
print()

nb_usr = -min
while nb_try > 0 and rand_nb != nb_usr:
	nb_usr = ask_number()
	if nb_usr > rand_nb:
		print("nombre est plus petit")
	if nb_usr < rand_nb:
		print("nombre est plus grand")
	nb_try -= 1
	print(f"Les chances restant ({nb_try})")
	print()

if nb_usr == rand_nb:
	print("tu as trouve le nombre magic : 💥")
else :
	print(f"Tu ea dead 🤬")
	print(f"le nombre magic est {rand_nb}")
	print(f"le nombre de vie restant {nb_try}")


