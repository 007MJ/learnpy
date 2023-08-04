import random

def x_or_ad():
	m_or_a = random.randint(0,1)
	if m_or_a == 1:
		return 1
	return 0


def min():
	return random.randint(0,10)

def max():
	return random.randint(0,10)



def	multi(nb, min_x, max_x):
	print(f"**************************Question {nb}")
	print(f"Question {min_x} * {max_x}")
	usr = input()
	try:
		int_sur = int(usr)
	except:
		print ("Entre des chiffre")
	else:
		return int_sur
	print()

def	add(nb, min_x, max_x):

	print(f"+++++++++++++++++++++++Question {nb}")
	print(f"Question {min_x} + {max_x}")
	usr = input()
	try:
		int_sur = int(usr)
	except:
		print ("Entre des chiffre")
	else:
		return int_sur
	print()

def mult_or_add(min , max, math):
	if math == 1:
		return min * max
	return min + max

def check_answer(answer, min, max, math):
		ok = mult_or_add(min , max, math)
		if answer == ok:
			print("bonne reponse")
		if answer != ok:
			print("mauvaise reponse")

g_answer = 0
nb_quest = 4

nb = 0
m_answer = 0
while nb_quest >= nb:
	math = x_or_ad()
	min_x = min()
	max_x = max()
	if math == 1:
		m_answer = multi(nb, min_x, max_x)
	if math == 0:
		m_answer = add(nb, min_x, max_x)
	check_answer(m_answer, min_x, max_x, math)

	nb +=1






