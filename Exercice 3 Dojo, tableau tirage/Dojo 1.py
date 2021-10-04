from random import randint

def main():
    peoples = ["Quentin", "Adrien", "Jojo", "Jordan", "David", "Timothée", "Cécilia", "Théo", "Nicolas", "Gael"]
    for i in range(len(peoples)):
        random_index = randint(0, len(peoples) - 1)
        pop_people = peoples.pop(random_index)
        number = f"{i+1}ère" if i == 1 else "" f"{i+1}ème" if len(peoples) != 0 else "dernière"
        end_string = f"Il reste {len(peoples)} personnes !" if len(peoples) != 0 else ""
        print(f"La {number} personne à sortir est {pop_people}. {end_string}")

if __name__ == "__main__":
    main()