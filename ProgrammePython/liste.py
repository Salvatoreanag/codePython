#coding:utf-8

"""
inventaire=range(40)     # range(n) crée une liste de 0 à n-1
for valeur in inventaire:
    print(valeur)

"""

"""
inventaire=["bac",10]*3
print(inventaire)
"""



abo=["epe","lissa",56,"ablawa",98,18,10,"abicou"]

print(abo[5])       #affiche l'élément à l'indice 5
print(abo[:])       #affiche tous les éléments de la liste
print(abo[:3])      #affiche les trois premiers éléments de la liste
print(abo[3:])      #affiche les éléments à partir du 4e élément
print(abo[-4])      #affiche l'élément à la 4e position en commençant par la fin
print(abo[2:6])     #affiche à partir du 2e élément jusqu'au (6-1)e élément
print(abo[5:2])     #affiche une liste vide
print("     ")

abo.append("java script")     # append() ajoute un élément à la liste
print(abo[:])
print("     ")

abo.insert(1,"Romain")        # insert() insère Romain à l'indice 1
print(abo[:])
print("     ")

abo.remove("abicou")          # remove() supprime l'élément en paramère
print(abo[:])
print("     ")

del abo[3]                    # supprime l'élément à l'indice 3
print(abo[:])
print("     ")

list1=["barc","Abo","Marceline","Jonh","Quebec","azerty"]
list2=[45,12,78,-58,45,445,-8469,45,5042]
list1.sort()                   # sort() permet de trier une list
list2.sort()
print(list1[:])
print(list2[:])
print("     ")

list1.reverse()               # reverse() inverse les éléments d'une liste
list2.reverse()
print(list1[:])
print(list2[:])
print("     ")

print("Nombre de répétition de 45:",list2.count(45))  # count() renvoie le nombre d'occurence de l'élément en paramètre
print("     ")

"""
list1.clear()                   # clear() vide la liste
print(list1[:])
print("     ")
"""


bloc = "::".join(list1)         # join() fait la jointure mais uniquement sur les chaines
print(bloc)

list1.extend(list2)             # extend() concatène deux listes
print(list1[:])                 # On peut aussi faire list1+=list2



#help(list)    renvoie les fonctions utilisables sur les listes
