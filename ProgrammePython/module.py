#coding:utf-8

# Une fonction lambda prend des paramètre ou non et exécutent une seule instructiuon
# C'est comme une fonction anonyme.On la stocke dans une variable qu'on appelle maintenant
# comme une fonction

coucou=lambda :print("Bonjour gars")
coucou()

ttc=lambda prixht:prixht+0.18*prixht
print(ttc(42512))

calcul=lambda x,y,z:20*x+3*y-17/z
print(calcul(12,-45,58))

#Passons maintenant à la modularité

from math import * # import math est ausssi possible mais on écrit math.sqrt()
resultat=sqrt(124)
print(resultat)
