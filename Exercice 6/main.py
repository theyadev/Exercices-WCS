from math import floor
from random import choice
import json
import random

# 1 - Créer une course pour les animaux

# 2 - Demander quelle est la distance de la course
#     (entre 100 et 1000km)

# 3 - Faire courrir les animaux (chaque tour dure une heure)
#     Il faut bien entendu :
#         - gérer pour chacun la distance parcourue et l'ordre d'arrivée
#         - créer une méthode permettant de les faire avancer

# 4 - A chaque étape de la course, afficher la liste des animaux (et s'il est arrivé) sous la forme :
#     {Nom}, le {Espèce} {Couleur}, a parcouru {Distance}km (et est arrivé en position {Position})

# 5 - A la fin de la course 
#     (lorsque tous les animaux ont franchi la ligne d'arrivée)
#     Afficher le résultat sous la forme :
#     La course a durée {heures} heures, le podium est :
#     {Position} - {Nom}, le {Espèce} {Couleur}, arrivé en {Heures} heures

#     La liste doit être triée par ordre d'arrivée

class AnimalsList:
    def __init__(self):
        self.animals = []

    def printAnimals(self):
        n = len(self.animals)

        if n == 0:
            return "Il n'y a pas d'animaux dans la liste ! --'"

        text = ""

        if n > 1:
            text += f"Les {n} animaux de la liste :D :\n"
        else:
            text += "Le seul animal de la liste :) :\n"

        for animal in self.animals:
            text += animal.printAnimal() + "\n"

        return text

    def addAnimal(self, animal):
        index = len(self.animals) + 1
        animal.nb = index
        self.animals.append(animal)

    def hasName(self, string: str):
        return True if any(animal for animal in self.animals if animal.name == string.capitalize()) else False

    def oldAnimals(self, years: int, family: str = None, color: str = None, name: str = None):
        filtered_animals: list[Animal] = self.animals
        
        if family is not None:
            filtered_animals: list[Animal] = list(filter(lambda x: x.family == family, filtered_animals))

        if color is not None:
            filtered_animals: list[Animal] = list(filter(lambda x: x.color == color, filtered_animals))

        if name is not None:
            filtered_animals: list[Animal] = list(filter(lambda x: x.name == name, filtered_animals))

        for animal in filtered_animals:
            animal.age += years
                     

class Animal:
    def __init__(
        self, 
        nb: int = None, 
        family: str = None, 
        color: str = None, 
        max_speed: int = 20, 
        age: int = 1,
        name: str = None
        ) -> None:
        self.name = name
        self.nb = nb
        self.family = family
        self.color = color
        self.max_speed = max_speed
        self.age = age
        
    def printAnimal(self):
        return f"{self.name} {self.nb} {self.color} a {self.age} an{'s' if self.age > 1 else ''}"

def readJSON(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []

types_animals = readJSON("./animaux.json")

family_list = ["Lapin", "Chat", "Mésange", "Python", "Chien", "Tourterelle", "Coccinelle", "Abeille"]
colors_list = ["Blanc", "Vert", "Bleu", "Rouge", "Jaune"]

def main():
    nb_animaux = input("Combien d'animaux voulez-vous faire naître ? : ")

    if not nb_animaux.isnumeric():
        print("Vous n'avez pas rentré un nombre... --'")
        return
        
    animals = AnimalsList()
    
    nb_animaux = int(nb_animaux)

    for i in range(nb_animaux):
        family = choice(list(types_animals.keys()))

        family_dict = types_animals[family]

        name = family

        if len(family_dict['names']) > 0:
            name = family_dict['names'].pop(floor(random.random() * len(family_dict['names'])))
            

        animals.addAnimal(Animal(family=family, color=choice(family_dict['colors']), name=name, max_speed=family_dict['max_speed']))
    print(animals.printAnimals())

    years_old = 1000000

    while years_old > 0:
        criteria = input("Quelles animaux voulez-vous faire vieillir ? : ")
        years_old = input("De combien d'années souhaitez-vous faire vieillir les animaux ? : ") 

        if not years_old.isnumeric():
            print("L'age doit être un nombre !")
            years_old = 1000
            continue

        years_old = int(years_old)

        args = criteria.split(" ")

        color = None
        family = None
        name = None

        for arg in args:
            if arg.capitalize() in family_list:
                family = arg.capitalize()
                continue
                
            if arg.capitalize() in colors_list:
                color = arg.capitalize()
                continue

            if animals.hasName(arg):
                name = arg.capitalize()
                continue

        animals.oldAnimals(years_old, family, color, name)

        print(animals.printAnimals())

    length_race = ""

    while not length_race.isnumeric() and length_race:
        input("Quel sera la taille de la course ? ")
    

    

if __name__ == "__main__":
    main()