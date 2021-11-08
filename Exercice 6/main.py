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


class Animal:
    lst = []

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
        self.nb = len(self.lst) + 1
        self.family = family
        self.color = color
        self.max_speed = max_speed
        self.age = age

        self.lst.append(self)

    def printAnimal(self):
        return f"{self.name} {self.nb} {self.color} a {self.age} an{'s' if self.age > 1 else ''}"

    @classmethod
    def printAnimals(cls):
        n = len(cls.lst)

        if n == 0:
            return "Il n'y a pas d'animaux dans la liste ! --'"

        text = ""

        if n > 1:
            text += f"Les {n} animaux de la liste :D :\n"
        else:
            text += "Le seul animal de la liste :) :\n"

        for animal in cls.lst:
            text += animal.printAnimal() + "\n"

        return text

    @classmethod
    def hasName(cls, string: str):
        return True if any(animal for animal in cls.lst if animal.name == string.capitalize()) else False

    @classmethod
    def oldAnimals(cls, years: int, family: str = None, color: str = None, name: str = None):
        filtered_animals: list[Animal] = cls.lst

        if family is not None:
            filtered_animals: list[Animal] = list(
                filter(lambda x: x.family == family, filtered_animals))

        if color is not None:
            filtered_animals: list[Animal] = list(
                filter(lambda x: x.color == color, filtered_animals))

        if name is not None:
            filtered_animals: list[Animal] = list(
                filter(lambda x: x.name == name, filtered_animals))

        for animal in filtered_animals:
            animal.age += years


def readJSON(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


types_animals = readJSON("./animaux.json")

family_list = ["Lapin", "Chat", "Mésange", "Python",
               "Chien", "Tourterelle", "Coccinelle", "Abeille"]
colors_list = ["Blanc", "Vert", "Bleu", "Rouge", "Jaune"]


def main():
    nb_animaux = input("Combien d'animaux voulez-vous faire naître ? : ")

    if not nb_animaux.isnumeric():
        print("Vous n'avez pas rentré un nombre... --'")
        return

    nb_animaux = int(nb_animaux)

    for i in range(nb_animaux):
        family = choice(list(types_animals.keys()))

        family_dict = types_animals[family]

        name = family

        if len(family_dict['names']) > 0:
            name = family_dict['names'].pop(
                floor(random.random() * len(family_dict['names'])))

        Animal(family=family, color=choice(
            family_dict['colors']), name=name, max_speed=family_dict['max_speed'])
    print(Animal.printAnimals())
    years_old = None

    while years_old is None or years_old > 0:
        criteria = input("Quelles animaux voulez-vous faire vieillir ? : ")
        years_old = input(
            "De combien d'années souhaitez-vous faire vieillir les animaux ? : ")

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

            if Animal.hasName(arg):
                name = arg.capitalize()
                continue

        print(color, family, name)
        Animal.oldAnimals(years_old, family, color, name)

        print(Animal.printAnimals())

    length_race = ""

    while not length_race.isnumeric() and length_race:
        input("Quel sera la taille de la course ? ")


if __name__ == "__main__":
    main()
