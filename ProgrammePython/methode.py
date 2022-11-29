#coding:utf-8

class Humain:
    lieu_habitation="Terre"
    def __init__(self,nom,prenom):
        self.name=nom
        self.surname=prenom

    def parler(self,message):    #On définit ici une méthode d'instance ou standrd puisqu'elle fonctionne sur une instance de la classe
        print("{} a dit à {} qu'{}".format(self.name,self.surname,message))

    #def changer_planete(cls,newplanete):  #On définit ici une méthode de classe mais elle n'est pas reconnu par l'interpretteur en tant que méthode de classe
        #Humain.lieu_habitation=newplanete

    #change_planet=classmethod(changer_planete)   #On assigne dans cet attribut de classe la methode changer_planete pour qu'elle puisse s'interpreter comme méthode de classe

    """ Une méthode statique est une fonction liée à une classe mais indépendante de celle-ci et de toute instance de la classe"""
    def definition():  #On definit ici une méthode statique mais n'est pas reconnue par l'interpretteur
        print("S'il n'est pas fou alors c'est qu'il est malade ")

    define=staticmethod(definition)  #On assigne dans cet attribut de classe la methode definition pour qu'elle puisse s'interpreter comme méthode statique

humain1=Humain("Brice","Georges")
humain1.parler("il est un peu souffrant")
humain1.parler("il doit se rendre chez ses parents demain")

print("Planette actuelle:{}".format(Humain.lieu_habitation))
Humain.lieu_habitation="Mars"
print("Planete actuelle:{}".format(Humain.lieu_habitation))