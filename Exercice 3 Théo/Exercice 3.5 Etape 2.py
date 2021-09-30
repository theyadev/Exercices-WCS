upper_sheet = "┌────────────────────────┐"
lower_sheet = "└────────────────────────┘"
duplicate_sheet = [
    ["││"],
    ["│────────────────────────│"]
]

people = [
    {
        "name": "Theo",
        "right": False
    },
     {
        "name": "Tom",
        "right": True
     },
      {
        "name": "Luc",
        "right": False
    },
     {
        "name": "David",
        "right": False
    }
]

people_r = [
    {
        "name": "Théo"
    }
]



def printSheet(left, right):
    print((len(left) + 3) * "\033[A" , end="")
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
printSheet(people, people_r)
