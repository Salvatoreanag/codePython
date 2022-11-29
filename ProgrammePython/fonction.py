#coding:utf-8

"""
def salutation(nom="Tom",message="Salut!"):
    print("{}:{}".format(nom,message))

salutation()  #Ici la fonction prend les paramètres par défaut
salutation("Jean Michel","Bonjour!Comment vas-tu?")
salutation("Norbert Brice","Je vais bien Gars")
"""

def show_inventory(*list_item):
    for item in list_item:
        print(item)

show_inventory("papa","maman","tante","Grace")