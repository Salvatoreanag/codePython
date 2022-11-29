#coding:utf-8

"""
1er code
compteur=0
while compteur<100:
    print("Je suis Edmond SATTO")
    compteur+=1
print("Je ne suis plus dans la boucle")


2eme code
jeuLancer=True

while jeuLancer:
    choixMenu=input("Votre choix>>")
    if choixMenu=="encore":
        continue  #revenir au début de la boucle
    elif choixMenu=="quitter":
        break     #casser la boucle
    elif choixMenu=="bonjour":
        print("Boujour gars")
    else:
        print("Commande introuvable")
print("A bientôt!")
"""
phrase="Jacques n'est pas à la maison"
for letter in phrase:
    print(letter)