class banque():
	def __init__(self, nom = "bob", solde = 500) :
		self.nom = nom
		self.solde = solde
	def depot(self,depot):
		self.solde = self.solde+depot
	def retrait(self,retrait):
		self.solde = self.solde-retrait
	def affiche(self):
		print(self.nom,self.solde)
"""compte num 1"""
compte1 = banque("Thomas", 10000)
compte1.retrait(3000)
compte1.depot(1250)
compte1.affiche()