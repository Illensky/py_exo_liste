noms = []


def demander_nom():
    new_name = input('donnez un nom : ')
    noms.append(new_name)
    if new_name == "":
        return
    demander_nom()


demander_nom()
noms.sort() #ordre alphabétique A-Z a-Z
print("liste de noms :")
for nom in noms:
    print(" " + nom)
