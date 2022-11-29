#coding:utf-8

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabet_crypte1 = []
alphabet_crypte2 = []
alphabet_crypte3 = []

# Création du 1er alphabet crypté
i=5
while (i<=25):
    alphabet_crypte1.append(alphabet[i])
    i += 1

j=0
while (j<5):
    alphabet_crypte1.append(alphabet[j])
    j += 1

# Création du 2e alphabet crypté
i=4
while (i<=25):
    alphabet_crypte2.append(alphabet[i])
    i += 1

j=0
while (j<4):
    alphabet_crypte2.append(alphabet[j])
    j += 1

# Création du 3e alphabet crypté
i = 22
while (i <= 25):
    alphabet_crypte3.append(alphabet[i])
    i += 1

j = 0
while (j < 22):
    alphabet_crypte3.append(alphabet[j])
    j += 1

print(alphabet)
print(alphabet_crypte1)
print(alphabet_crypte2)
print(alphabet_crypte3)

mot = "PAPAMAMIEST"
motlist=list(mot)
i=0

while (i <= len(motlist)):
    inf = 0
    sup = 25
    trouve = False
    while (trouve == False and sup >= inf):
        milieu = int((inf + sup) / 2)
        if (motlist[i] == alphabet[milieu]):
            trouve=True
        elif (motlist[i] < alphabet[milieu]):
            sup = milieu-1
        else:
            inf = milieu+1
    print(alphabet_crypte1[milieu])

    j=i+1
    inf = 0
    sup = 25
    trouve = False
    while (trouve == False and sup >= inf):
        milieu = int((inf + sup) / 2)
        if (motlist[j] == alphabet[milieu]):
            trouve = True
        elif (motlist[j] < alphabet[milieu]):
            sup = milieu - 1
        else:
            inf = milieu + 1
    print(alphabet_crypte2[milieu])

    k=j+1
    inf = 0
    sup = 25
    trouve = False
    while (trouve == False and sup >= inf):
        milieu = int((inf + sup) / 2)
        if (motlist[k] == alphabet[milieu]):
            trouve = True
        elif (motlist[k] < alphabet[milieu]):
            sup = milieu - 1
        else:
            inf = milieu + 1
    print(alphabet_crypte3[milieu])

    i=k+1