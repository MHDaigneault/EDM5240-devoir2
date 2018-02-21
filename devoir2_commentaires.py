### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#coding: utf-8
import csv
#importer le fichier

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier="../grants.csv"
#identifier le fichier a importer

f1 = open(fichier,encoding = "utf-8")
#ouvrir le fichier

lignes = csv.reader(f1)
#l'intégralité du document s'appel lignes.

editeurs = "Aide aux éditeurs"
innovation = "Innovation commerciale"
initiative = "Initiatives collectives"
n=0
#Il s'agit des trois programmes.

for subvention in lignes:
#début de la boucle.

#https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
	if any(editeurs in element for element in subvention):
		
		date = subvention[13]
		#la date est le 13e élément

### Bonne idée d'utiliser «.split()» pour isoler la date!
### Une autre méthode: «annee = annee[:4]»

		annee = date.split("-")

### Super que de décorer ton «output» :)

		#séparer la date avec des -.

### Bravo d'avoir pensé mettre le compteur à l'intérieur des conditions pour ne compter que les subventions que tu cherches
		n+=1

		print("-" * 10)
		print(n,annee[0], subvention)
		print(editeurs)
### Pour tester ce que va chercher ton code, j'imprime la ligne ci-dessous
		# print(subvention[17])

	if any(innovation in element for element in subvention):

		date = subvention[13]
		annee = date.split("-")
		n+=1
		
		print("-" * 10)
		print(n,annee[0], subvention)
		print(innovation)
		# print(subvention[17])


	if any(initiative in element for element in subvention):
		date = subvention[13]
		annee = date.split("-")
		n+=1
			
		print("-" * 10)
		print(n,annee[0], subvention)
		print(initiative)
		# print(subvention[17], subvention)

### Cet enchaînement de conditions faisait en sorte que tu n'obtenais pas tout à fait les bonnes subventions
### Certaines «Initiatives collectives» ne concernent pas le Fonds du Canada pour les périodiques et touchent plutôt le monde du livre
### La solution, un seul «if», mais avec un «or»:
### «if "Fonds du Canada pour les périodiques" in subvention[17] or "FCP -" in subvention[17]:»