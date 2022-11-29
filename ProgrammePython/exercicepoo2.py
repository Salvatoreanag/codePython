#coding:utf-8

class Satellite:
    def __init__(self,nom,masse=100,vitesse=0):
        self.name=nom
        self.mass=masse
        self.speed=vitesse

    def impulsion(self,force,duree):
        self.speed_variation=(force*duree)/self.mass

    def afficherVitesse(self):
        print("{} a une vitesse de {} mètres par seconde".format(self.name,self.speed_variation))

    def energie(self):
        self.energie_cinetique=(self.mass*(self.speed_variation**2))/2
        return self.energie_cinetique

#Programme principal
satellite1=Satellite("Zoé",985,8)
satellite1.impulsion(500,15)
satellite1.afficherVitesse()
print(satellite1.energie(),"Joules")