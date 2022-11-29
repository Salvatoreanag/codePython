#coding:utf-8

#classe mère
class Vehicule:
    def __init__(self,nom,quantite_essence,poids):
        self.name=nom
        self.qte_ess=quantite_essence
        self.weight=poids

    def seDeplacer(self):
        print("Le vehicule se déplace à une grande vitesse")

#classe fille
class Voiture(Vehicule):
    def __init__(self,nom_voi,ess_voi,poids_voi,vitesse,puissance):   #Le constructeur de la classe fille doit contenir les mêmes paramètres que celle de la classe mère en plus de ses propres paramètres
        Vehicule.__init__(self,nom_voi,ess_voi,poids_voi)             # Au lieu de redefinir les attributs communs aux deux classes,on appelle juste le constructeur de la classe mère avec les paramètre concernés
        self.speed=vitesse
        self.power=puissance

    def seDeplacer(self):
        print("Je suis une voiture.Je roule sur le goudron")  #Redéfinition de méthode dans la classe fille

#Programme principal
    #Objet vehicule
vehicule1=Vehicule("Toyota","200 litres","1256 kg")
print("{} consomme {} d'essence et pèse {}".format(vehicule1.name,vehicule1.qte_ess,vehicule1.weight))
vehicule1.seDeplacer()

    #Objet voiture
voiture1=Voiture("Venza","150 litres","1232 kg","30 m/s","20 chevaux")
print("{} consomme {} d'essence et pèse {}".format(voiture1.name,voiture1.qte_ess,voiture1.weight))
print("De plus elle a une vitesse de {} et une puissance de {}".format(voiture1.speed,voiture1.power))
voiture1.seDeplacer()

    #Vérifier si un objet est une instance d'une classe donnée
if isinstance(voiture1,Voiture):  # On fait cette vérification grâce à la fonction isinstance()
    print("J'y suis effectivement")

    #Vérifier si une classe hérite vraiment d'une classe donnée
if issubclass(Voiture,Vehicule):   # On fait cette vérification grâce à la fonction issubclass()
    print("Je suis un héritier")