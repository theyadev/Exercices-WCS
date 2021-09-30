import os
from time import sleep
from random import randint

upper_sheet = "┌────────────────────────┐"
lower_sheet = "└────────────────────────┘"
duplicate_sheet = [
    ["││"],
    ["│────────────────────────│"]
]

def printSheet(left, right):
    print((len(left) + 11) * "\033[A" , end="")
    left.sort(key=lambda x: x["name"])
    print(upper_sheet + 20*" " + upper_sheet)
    for i in range(len(left)):
        row = ""
        for j in range(2):
            if j == 1:
                row+= 20*" "
            if j == 0:
                color = '\033[47m\033[30m' if left[i]['right'] == True else ''
                row += f"{duplicate_sheet[0][0][0]}{color}{left[i]['name'].center(24)}\033[0m{duplicate_sheet[0][0][1]}"
            else:
                try:
                    row += f"{duplicate_sheet[0][0][0]}{right[i]['name'].center(24)}{duplicate_sheet[0][0][1]}"
                except:
                    row += f"{duplicate_sheet[0][0][0]}{24*' '}{duplicate_sheet[0][0][1]}"
        if i < len(left) -1:
            row += f"\n{duplicate_sheet[1][0]}{20*' '}{duplicate_sheet[1][0]}"
        print(row)
    print(lower_sheet + 20*" " + lower_sheet)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    # "Quentin", "Adrien", "Jojo", "Jordan", "David", "Timothée", "Cécilia", "Théo", "Nicolas", "Gael"
    peoples = [
        {
            "name": "Quentin",
            "right": False
        },
        {
            "name": "Adrien",
            "right": False
        },
        {
            "name": "Jojo",
            "right": False
        },
        {
            "name": "Jordan",
            "right": False
        },
        {
            "name": "David",
            "right": False
        },
        {
            "name": "Timothée",
            "right": False
        },
        {
            "name": "Cécilia",
            "right": False
        },
        {
            "name": "Théo",
            "right": False
        },
        {
            "name": "Nicolas",
            "right": False
        },
        {
            "name": "Gael",
            "right": False
        },
    ]
    peoples_in = []

    def popInArray(index, n):
        peoples_in.append(peoples[index])
        peoples[index]['right'] = True
        return peoples[index]

    printSheet(peoples, peoples_in)
    for i in range(len(peoples)):
        sleep(1)
        random_number = randint(0, len(peoples)-1)
        while peoples[random_number]["right"] == True:
            random_number = randint(0, len(peoples)-1)
        popInArray(random_number, i + 1)
        printSheet(peoples, peoples_in)


if __name__ == "__main__":
    main()