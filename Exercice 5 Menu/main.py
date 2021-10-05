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

persons_list = []

def showList():
    sort_list = input("Voulez-vous trier la liste ? ").lower()
    new_list = list(persons_list)
    if sort_list == 'y' or sort_list == "yes" or sort_list == 'o' or sort_list == "oui":
        sort_possibility = [('Nom', "name", False), ("Nom de Famille", "surname", False), ("Age", "age", True), ("Points", "points", True)]
        for index, e in enumerate(sort_possibility):
            print(f"{index+1} : Trier par {sort_possibility[index][0]}")
        print()
        try:
            choose_index = int(input("Index choisie: ")) -1
            if choose_index < 0 or choose_index >= len(sort_possibility):
                return print("L'index choisis n'etait pas dans la liste !")
        except:
            return print('Nombre invalide !')
        persons_list.sort(key=lambda x: x[sort_possibility[choose_index][1]], reverse=sort_possibility[choose_index][2])

    print()
    for person in persons_list:
        print(f"{person['name']} {person['surname']}, {person['age']}ans ({person['gender'].upper()}) | {person['points']}pts")
    persons_list.clear()
    persons_list.extend(new_list)

def addPerson():
    try:
        name = input("Prénom de la personne que vous voulez ajouter ?\033[K ")
        if len(name) <= 2:
            return print("Le nom doit faire minimum 2 caractères !")
        surname = input("Nom de famille ?\033[K ")
        if len(surname) <= 2:
            return print("Le nom de famille doit faire minimum 2 caractères !")
        age = int(input("Age ?\033[K "))
        gender = input("Sexe ? (M/F)\033[K ")
        if gender.lower() != "m" and gender.lower() != 'f':
            return print("Le genre doit être M ou F ! ")
        print("\033[K\n\033[K")
        persons_list.append({
            "name":name,
            "surname": surname,
            "age": age,
            "gender": gender.lower(),
            "points": 0
        })
        print("La personne à bien été ajouté !")
    except ValueError:
        print("\n\nL'age doit être un nombre entier !")

def chooseBetweenMultiples(index_names):
    choose_index = 0
    print('Il y a plusieurs personnes de ce nom la, veuillez choisir: \n')
    for index in index_names:
        print(f"{index+1}: {persons_list[index]['name']} {persons_list[index]['surname']}, {persons_list[index]['age']}ans ({persons_list[index]['age']})")

    try:
        choose_index = int(input("Index de la personne choisie: ")) -1
        if not choose_index-1 in index_names:
            return print("L'index choisis n'etait pas dans la liste !")
    except:
        return print('Nombre invalide !')
    
    print()
    return choose_index
    

def delPerson():
    name = input("Prénom de la personne que vous voulez supprimer ? ").lower()
    index_names = [i for i in range(len(persons_list)) if persons_list[i]['name'].lower() == name]
    if index_names == []: return print("Il n'y a personne de ce nom la, verifier l'orthographe !")
    index_to_del = index_names[0]
    if len(index_names) > 1:
        index_to_del = chooseBetweenMultiples(index_names)
    person_deleted = persons_list.pop(index_to_del)
    print(f"{person_deleted['name']} {person_deleted['surname']} a été supprimé !")

def addPoints():
    name = input("Prénom de la personne à qui vous voulez ajouter des points ? ").lower()
    index_names = [i for i in range(len(persons_list)) if persons_list[i]['name'].lower() == name]
    if index_names == []: return print("Il n'y a personne de ce nom la, verifier l'orthographe !")
    index_to_add = index_names[0]
    if len(index_names) > 1:
        index_to_add = chooseBetweenMultiples(index_names)
    
    points = 0
    try:
        points=int(input(f"Combien de points voulez ajouter à {persons_list[index_to_add]['name']}? "))
    except:
        return print('Nombre invalide !')
    persons_list[index_to_add]['points'] += points
    print(f"{persons_list[index_to_add]['name']} {persons_list[index_to_add]['surname']} a gagné {points} points ! {'Il' if persons_list[index_to_add]['gender'] == 'm' else 'Elle'} a maintenant {persons_list[index_to_add]['points']} points !")

def save():
    if persons_list == []: 
        return print("La liste est vide ! ")
    save_name = input('Nom de la sauvegarde ? ')
    with open(f'./Data/{save_name}.json', 'w', encoding="utf-8") as json_file:
        json.dump(persons_list, json_file, ensure_ascii=False, indent=4)
        print(f"La liste a été sauvegarder a l'emplacement ./Data/{save_name}.json")
    return

def load():
    saves = [f for f in os.listdir("./Data") if os.path.isfile(os.path.join("./Data", f))]
    for index, save in enumerate(saves):
        print(f"{index+1}: {save}")
    try:
        choose_index = int(input("Index de la save choisie: ")) -1
        if choose_index < 0 or choose_index >= len(saves):
            return print("L'index choisis n'etait pas dans la liste !")
    except:
        return print('Nombre invalide !')
    
    with open(f"./Data/{saves[choose_index]}", "r", encoding="utf-8") as s:
            persons_list.clear()
            persons_list.extend(json.load(s))
            print(f"{saves[choose_index]} a été charger !")
    

def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def main():
    pointer = "\033[5m←\033[0m"
    pointer_pos = 1
    menu = ["Afficher la liste de personnes.","Ajouter une personne.", "Supprimer une personne.", "Ajouter des points à une personne.", "Sauvegarder.", "Charger.", "Quitter."]
    
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
            for i in range(20):
                print('\033[K')
            printAt(1, len(menu) + 1, "")
            print()
            if pointer_pos == 1:
                print()
                showList()
            elif pointer_pos == 2:
                print()
                addPerson()
            elif pointer_pos == 3:
                delPerson()
            elif pointer_pos == 4:
                addPoints()
            elif pointer_pos == 5:
                save()
            elif pointer_pos == 6:
                load()
            elif pointer_pos == 7:
                quit()
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