import os
import random
from time import sleep
from random import randint

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printNames(left, right):
    clear()
    if len(left) != len(right):
        return print("Probleme, le code ne peut pas s'éxécuter correctement !")
    l = ""
    for index in range(len(left)):
        l+= f"{left[index]} {(20-len(left[index]))*' '} | {right[index]}\n"
    print(l)



def main():
    peoples = ["Quentin", "Adrien", "Jojo", "Jordan", "David", "Timothée", "Cécilia", "Théo", "Nicolas", "Gael"]
    peoples_in = []

    for i in range(len(peoples)):
        peoples_in.append('')

    def popInArray(index, n):
        peoples_in[index] = f"N°{str(n)}: {peoples[index]}"
        peoples[index] = ""
        return peoples_in[index]

    printNames(peoples, peoples_in)
    i = 0
    for people in peoples:
        sleep(1)
        random_number = randint(0, len(peoples)-1)
        while peoples[random_number] == "":
            random_number = randint(0, len(peoples)-1)
        popInArray(random_number, i + 1)
        printNames(peoples, peoples_in)
        i+=1


if __name__ == "__main__":
    main()