#coding:utf-8

"""
Un dictionnaire en python est assimilé à un tableau associatif en php

Création d'un dictionnaire     : dico={cle:valeur,cle1:valeur}
Accéder à une valeur           : dico[cle]
"""

dico={"Chat":"C'est un animal",1:"seconde","chien":"c'est un mamifère"}

print(dico)
print("   ")

for key in dico.keys():                # afficher toutes les clés d'un dictionnaire
    print(key)
print("   ")

for value in dico.values():             # afficher toutes les valeurs d'unn dictionnaire
    print(value)
print("    ")

for i,j in dico.items():                # afficher le dictionnaire par clé et par valeur
    print("Clé:{} -> Valeur:{}".format(i,j))
print("    ")

dico["bro"]="Je vais bien"              # ajout au dictionnaire
print(dico)
print("   ")

print(dico[1])                          # acceder à une valeur
print("   ")

dico.pop("chien")                       # pop() supprime la valeur associée à la clé renseignée en paramètre
print(dico)
print("   ")

valeur_supprimee=dico.pop("Chat")       # on réccupère ici la valeur supprimée
print(valeur_supprimee)
print("    ")





# help(dict)                    # avoir d'aide sur les fonctions