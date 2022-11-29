#coding:utf-8

class CompteBancaire:
    def __init__(self,nom="Dupont",solde=1000):
        self.name=nom
        self.balance=solde

    def depot(self,somme):
        self.sum_d=self.balance+somme
        self.balance=self.sum_d

    def retrait(self,somme):
        self.sum_r=self.balance-somme
        self.balance=self.sum_r

    def affiche(self):
        print("Mr. {},votre solde actuelle est {}".format(self.name,self.balance))

#Programme principal
compte1=CompteBancaire("ALLASANE Gian",548000)
montant_depose=int(input("Entrez le montant de dépôt:"))
compte1.depot(montant_depose)
compte1.affiche()

compte2=CompteBancaire("BALOGOUN Gérard",785412969)
montant_retire=int(input("Entrez le montant de retrait:"))
compte2.retrait(montant_retire)
compte2.affiche()
