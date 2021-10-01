import os
from random import randint
from time import sleep

animals_list_tuples = [("Lièvre", "marron", 60, "🐇",40),
                       ("Hérisson", "gris", 10, "🦔",5), ("Lapin", "blanc", 30, "🐰",20),
                       ("Guépard", "orange", 90, "🐆",60), ("Faucon", "noir", 120, "🦅",90),
                       ("Girafe", "jaune", 70, "🦒",50), ("Perroquet", "bleu", 50, "🦜",40)]

animals = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tuplesToObjs():
    for index, animal in enumerate(animals_list_tuples):
        name, color, speed, emote,min_speed = animal
        animals.append({
            "name": name,
            "color": color,
            "min_speed": min_speed,
            "speed": speed,
            "emote": emote,
            "position": index+1,
            "distance": 0,
            "finished": False,
            "turns": 0,
            "distance_done": 0
        })


def getRaceLength():
    try:
        race_length = int(input("Quel est la taille de la course en km ? (min 50) "))
        if race_length < 50:
            return getRaceLength()
        return race_length
    except:
        print("Nombre invalide !")
        return getRaceLength()


def printRace(race_length):
    print((len(animals) +2) * "\033[A\033[K" , end="")
    row = ""
    for animal in animals:
        race_row = int(round(race_length)/10) * '-'
        list_row = list(race_row)
        try:
            list_row[int(round(animal['distance'])/10)] = animal['emote']
        except:
            list_row.append(animal['emote'])
        race_row = ''.join(list_row)
        row += f"{animal['position']} | {race_row} (Parcouru: {animal['distance_done']}km) {'Finis !' if animal['finished'] == True else ''} \n"
    print(row)



def main():
    clear()
    tuplesToObjs()
    race_length = getRaceLength()
    printRace(race_length)
    animals.sort(key=lambda x: x["speed"], reverse=True)
    winners = []
    turns = 1
    while len(winners) < len(animals):
        sleep(1)
        for animal in animals:
            if animal['finished']== True:
                continue
            random_distance = randint(animal['min_speed'], animal['speed'])
            animal['distance'] += random_distance
            animal['distance_done'] = random_distance
            if animal['distance'] >= race_length:
                animal['turns'] = turns
                animal['finished'] = True
                winners.append(animal)
            animals.sort(key=lambda x: x["position"])
            printRace(race_length)
            animals.sort(key=lambda x: x["speed"], reverse=True)
        turns += 1
    print(f"Le gagnant est: {winners[0]['name']} en {winners[0]['turns']} heures !")
    print("Les suivants sont: ")
    for i in range(1, len(winners)):
        print(f'- {winners[i]["name"]} en {winners[i]["turns"]} heures !')
            




    


if __name__ == "__main__":
    main()
