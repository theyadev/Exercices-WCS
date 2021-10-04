#Add Person Name
#Del Person
#Add Points
#Show list, sorted if he wants
#Save in folder Data, named as he wants
#Load file from Data folder
# (nom, prénom, âge, sexe, score

import os
import json
from msvcrt import getch

from settings import *


def showList():
    print(persons_list)

def addPerson():
    try:
        name = input("Nom de la personne que vous voulez ajouter ?\033[K ")
        if len(name) <= 2:
            return print("Le nom doit faire minimum 2 caractères !")
        surname = input("Nom de famille ?\033[K ")
        if len(surname) <= 2:
            return print("Le nom de famille doit faire minimum 2 caractères !")
        age = int(input("Age ?\033[K "))
        gender = input("Sexe ? (M/F)\033[K ")
        if gender.lower() != "m" or gender.lower() != 'f':
            return print("Le genre doit être M ou F ! ")
        print("\033[K\n\033[K")
        print("La personne à bien été ajouté !")
    except ValueError:
        print("\n\nL'age doit être un nombre entier !")
def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def main():
    user_input = 0
    pointer = "\033[5m←\033[0m"
    pointer_pos = 1
    menu = ["Afficher la liste de personnes.","Ajouter une personne.", "Supprimer une personne.", "Ajouter des points à une personne.", "Sauvegarder.", "Charger."]
    
    os.system("cls")
    for i in range(len(menu)):
        printAt(0, i+1, menu[i])
        
    while True:
        printAt(len(menu[pointer_pos-1])+2, pointer_pos, pointer)

        for i in range(len(menu)):
            if i == pointer_pos -1:
                continue
            printAt(len(menu[i]), i+1, "   ")

        command = ord(getch())
        if command == 13:
            if pointer_pos == 1:
                print()
                showList()
            elif pointer_pos == 2:
                print()
                addPerson()
        elif command == 72:
            if pointer_pos == 1:
                continue
            else:
                pointer_pos -= 1
        elif command == 80:
            if pointer_pos == len(menu):
                continue
            else:
                pointer_pos += 1
        elif command == 108:
            quit()

if __name__ == "__main__":
    main()