#coding:utf-8
agePersonne=input("Entrez l'age de l'individu: ")
prixHt=input("Donnez le prix ht:")
prixHt=int(prixHt)
texte="L'age de la personne est {} et son prix hors taxe est {} fcfa"

print("Jonas a",agePersonne,"ans.")
print(texte.format(agePersonne,prixHt))

prixTTC=prixHt+(0.18*prixHt)
print("Le prix total est {}".format(prixTTC))
