animals_list_tuples = [("Lièvre", "marron", 60),
                       ("Hérisson", "gris", 10), ("Lapin", "blanc", 30),
                       ("Guépard", "orange", 90), ("Faucon", "noir", 120),
                       ("Girafe", "jaune", 70), ("Perroquet", "bleu", 50)]

animals = []


def tuplesToObjs():
    for animal in animals_list_tuples:
        name, color, speed = animal
        animals.append({
            "name": name,
            "color": color,
            "speed": speed
        })


tuplesToObjs()
animals.sort(key=lambda x: x["speed"], reverse=True)

for index,animal in enumerate(animals):
    end_str = ", et c’est lui le plus rapide !" if index == 0 else "" ", et c’est lui le plus lent !" if index == len(animals)-1 else "."
    print(f"Le {animal['name']} {animal['color']} court à {animal['speed']}km/h{end_str}")