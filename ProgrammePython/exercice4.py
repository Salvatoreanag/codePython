#Convertir un nombre entier de secondes fourni au départ en un nombre
#d'années,de mois,de jours,de minites et de secondes

#coding:utf-8

nbre_seconde=input("Entrez le nombre de seconde:")
nbre_seconde=int(nbre_seconde)

annee=int((nbre_seconde-(nbre_seconde%31563000))/31536000) #1an=31536000secondes
annee_reste=nbre_seconde%31536000

mois=int((annee_reste-(annee_reste%2592000))/2592000)      #1mois=2592000secondes
mois_reste=annee_reste%2592000

jour=int((mois_reste-(mois_reste%86400))/86400)            #1jour=86400secondes
jour_reste=mois_reste%86400

minute=int((jour_reste-(jour_reste%60))/60)                #1minute=60secondes
seconde=jour_reste%60

print(nbre_seconde,"secondes correspond à ",annee,"an(s)",
      mois,"mois ",jour,"jour(s) ",minute,"minute(s) et ",
      seconde,"seconde(s)")