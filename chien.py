class chien():
	def __init__(self,race ="labrador",couleur="blanc",poil="laineux"):
		self.race = race
		self.couleur = couleur
		self.poil = poil

	def choix_poil(self, choix_poil = input("Laineux ou soyeux ^^?")):
		self.poil = choix_poil

	def choix_race(self, choix_race = input("quelle est la race de votre chien")):
		self.race = choix_race

	def choix_couleur(self, choix_couleur = input("enter la couleur de votre chien")):
		self.couleur= choix_couleur

	def affiche(self):
		phrase = ("votre chien fait partie de la race " + self.race + " de plus c'est un chien " + self.couleur + " qui a le poil " + self.poil)
		print(phrase.lower())

darky = chien()
darky.choix_poil()
darky.choix_race()
darky.choix_couleur()
darky.affiche()