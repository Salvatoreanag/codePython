#coding:utf-8
"""
identifiant="ablawa"
mot_de_passe="125487"

print("Page de connexion:")

id=input("Entrez votre identifiant:")
mdp=input("Entrez votre mot de passe:")
if id==identifiant and mdp==mot_de_passe:
    print("Vous êtes connecté!Bienvenue ",id)
else:
    print("Votre identifiant ou votre mot de passe est erroné.")
"""

age=input("Entrez votre âge: ")
age=int(age)
if 0<age<=12:
    print("Tu es un adolescent")
    name="bake"
    nom=input("Quel est ton nom:")
    if name==nom:
        print(nom," tu es le fils de AGANON")
    else:
        print("Je ne te connais pas")
elif 13<age<=18:
    print("Tu es un enfant")
else:
    print("Tu es un adulte")

