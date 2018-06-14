class voiture :
	def __init__(self, color = "red", puissance = 250, marque = "ferrari") :
		self.color = color
		self.puissance = puissance
		self.marque = marque

	def chevaux(self,chevaux):
		self.puissance = self.puissance+chevaux

	def couleur(self, couleur):
		self.color = couleur
	def change_marque(self,change_marque):
		self.marque = change_marque
	def affiche(self):
		print(self.color,self.puissance,self.marque)

"""Personnalisation porsche 911"""

porsche = voiture()
porsche.change_marque("porsche")
porsche.chevaux(450)
porsche.couleur("NOIR")
porsche.affiche()