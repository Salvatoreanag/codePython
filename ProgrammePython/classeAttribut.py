#coding:utf-8

"""
#Classe et Attribut || Ici les attributs sont les attributs d'objet

class Humain:
     def __init__(self,nom,prenom,age):                 #__init__() c'est le constructeur || 'self' cible l'objet lui même qu'on est entrain de créer
          print("Création d'un humain")
          self.name=nom
          self.surname=prenom
          self.old=age

humain1=Humain("ASSIBA","Jacques",13)   #On crée un objet humain1
print("{} {} a {} ans".format(humain1.name,humain1.surname,humain1.old))
"""

#Les attributs de classe

class Humain:
     humain_cree = 0  # attribut de classe
     def __init__(self,nom="BAKE",prenom="Brice",age=18):   #On initialise les variables
          print("Création d'un humain")
          self.name=nom
          self.surname=prenom
          self.old=age
          Humain.humain_cree +=1    #On accède aux attributs de classe grâce au nom de la classe

humain1=Humain()
print("Humain existant: {}".format(Humain.humain_cree))

humain2=Humain()
print("Humain existant: {}".format(Humain.humain_cree))

humain3=Humain()
print("Humain existant: {}".format(Humain.humain_cree))
