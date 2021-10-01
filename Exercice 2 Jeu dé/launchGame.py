import math
from os import write
import random
import time

from clear import clear
from getDice import getDice
from getParticipants import getParticipants
from writeAnimation import writeAnimation
from showWinners import showWinners


def launchGame(participants=None, settings=None, old_winners=None, old_max_numbers=None):
    if (participants == None):
        clear()
        participants = getParticipants()

        if (len(participants) <= 1):
            print("Il n'y a pas assez de participants !")
            quit()

    if (settings == None):
        settings = {}
        settings["dice"] = getDice()
        clear()
        writeAnimation(
            "Bien ! Nous avons tous nos participants, nos parametres, commençons a jeter les dés !\n\n\n")

    for index in range(len(participants)):
        randomNumber1 = math.ceil(random.random()*(settings["dice"] or 6))
        randomNumber2 = math.ceil(random.random()*(settings["dice"] or 6))
        participants[index]["number"] = randomNumber1 + randomNumber2
        print_str_start = f'{participants[index]["name"]} a tiré un:\n\n'
        print_str_end = f'\033[0mPour un total de \033[32m{participants[index]["number"]}\033[0m'

        if participants[index]["number"] > ((settings["dice"]*2)/(1 + 1/3) or 9):
            print_str_end += " \033[31m!!\033[0m\n\n"
        elif participants[index]["number"] > ((settings["dice"]*2)/2 or 6):
            print_str_end += "\033[91m !\033[0m\n\n"
        else:
            print_str_end += ".\n\n"

        writeAnimation(print_str_start)
        random_int = random.randint(10, 30)
        for i in range(random_int):
            r = math.ceil(random.random()*(settings["dice"] or 6))
            time.sleep(0.1)
            if i < random_int-1:
                print(f'\033[96m{r}  ', end='\r')
            else:
                print('     ', end='\r')
                print(f'\033[92m{randomNumber1}   \n')

        writeAnimation('\033[0met un:\n\n')
        random_int = random.randint(10, 30)
        for i in range(random_int):
            r = math.ceil(random.random()*(settings["dice"] or 6))
            time.sleep(0.1)
            if i < random_int-1:
                print(f'\033[96m{r}   ', end='\r')
            else:
                print('     ', end='\r')
                print(f'\033[92m{randomNumber2}   \n')

        writeAnimation(print_str_end)
        print('\n-----------------\n\n')

    max_number = max(participant["number"] for participant in participants)
    winners_name = []

    for index in range(len(participants)):
        if(participants[index]["number"] == max_number):
            participants[index]["winner"] = True
            winners_name.append(participants[index]["name"])

    if len(winners_name) == 1:
        writeAnimation("Le vainqueur est...\n")
        print(f'\033[33m{winners_name[0]} \033[0m!\n\n')
    else:
        writeAnimation('Les vainqueurs sont...\n')
        print(f'\033[33m{" et ".join(winners_name)}\033[0m!!\n\n')

    writeAnimation('Voulez-vous rejouer ? (oui/non) ')
    res = input()

    if res.lower() == "oui" or res.lower() == "o":

        writeAnimation(
            "Voulez-vous rejouer avec les memes participants et les memes parametres ? (oui/non) ")
        resSameParts = input()
        if resSameParts.lower() == "oui" or resSameParts.lower() == "o":
            writeAnimation("Et bien nous sommes repartis !\n\n")
            if (old_winners == None):
                old_winners = []
            if (old_max_numbers == None):
                old_max_numbers = []
            old_max_numbers.append(max_number)
            old_winners.append(winners_name)
            launchGame(participants, settings, old_winners, old_max_numbers)
        elif resSameParts.lower() == "non" or resSameParts.lower() == "n":
            writeAnimation("Pas de probleme, on recommence !\n")
            launchGame()
        else:
            launchGame()

    elif res.lower() == "non" or res.lower() == "n":
        writeAnimation("Aurevoir ! C'était une belle partie !\n\n")
        time.sleep(0.3)
        showWinners(winners_name, max_number, old_winners, old_max_numbers)
        return

    else:
        writeAnimation(
            "Tu n'as pas répondu oui ni non, je vais donc me désactiver ! Aurevoir !\n\n")
        time.sleep(0.3)
        showWinners(winners_name, max_number, old_winners, old_max_numbers)
        return
