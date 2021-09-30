from datetime import date

def er_eme(i):
    er_eme = ""

    if i == 1:
        er_eme = "ère"
    else:
        er_eme = "ème"

    return er_eme

def getNbPers():
    p = input("Combien il y a de personnes dans la salle ?\n")
    try:
        p = int(p)
        return p
    except:
        print("Ce n'est pas un nombre !")
        return getNbPers()


def getName(i):
    n = input(f"Comment la {i}{er_eme(i)} personne s'appelle-t-elle ?\n")
    try:
        n = int(n)
        print('Nom invalide.')
        return getName(i)
    except:
        return n


def getAge(i):
    a = input(f"Quel age a la {i}{er_eme(i)} personne ?\n")
    try:
        a = int(a)
        return a
    except:
        print("Age invalide")
        return getAge(i)


class Personne:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.age}ans"


print('Bonjour !')

nb_pers = getNbPers()

pers = []

for i in range(0, nb_pers):
    name = getName(i+1)
    age = getAge(i+1)

    pers.append(Personne(name, age))
    i = i+1

print("Dans la salle il y a:")

year = date.today().year

for per in pers:
    print(f"{per.name}, {per.age}ans.\nIl/Elle est né(e) en {year-per.age}!")
