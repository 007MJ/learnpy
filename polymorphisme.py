# polymorphisme
# plusieur types -> la meme interface (meme code)

class Etrevivan():
	def print_infos(self):
		print("JE suis un etre vivant")

class Chat(Etrevivan):
	def print_infos(self):
		print("je suis un chat")

class Personne(Etrevivan):
	def print_infos(self):
		print("je suis une personne")

l = [Etrevivan(), Chat(), Personne()]

for e in l:
	e.print_infos()

def additioner(a, b):
	somme = 0
	if isinstance(a, int):
		somme += a
	if isinstance(a, str):
		somme += len(a)
	return somme
