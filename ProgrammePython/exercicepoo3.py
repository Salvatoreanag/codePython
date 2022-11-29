#coding:utf-8

from exercicepoo1 import *
class CompteEpargne(CompteBancaire):
    def __init__(self,nom_ce,solde_ce,taux=0.003):
        CompteBancaire.__init__(self,nom_ce,solde_ce)
        self.percent=taux

    def changeTaux(self,valeur):
        self.taux=valeur

    def capitalisation(self,nombre_mois):
        self.taux=self.taux*100
        print("Pour {} mois,on considère un taux de {} %".format(nombre_mois,self.taux))
        solde=
