from random import randint

def main(peoples):
    for i in range(len(peoples)):
        print(f'La {f"{i+1}ère" if i == 1 else "" f"{i+1}ème" if len(peoples) != 0 else "dernière"} personne à sortir est {peoples.pop(randint(0, len(peoples) - 1))}. {f"Il reste {len(peoples)} personnes !" if len(peoples) != 0 else ""}')

if __name__ == "__main__":
    main(["Quentin", "Adrien", "Jojo", "Jordan", "David", "Timothée", "Cécilia", "Théo", "Nicolas", "Gael"])