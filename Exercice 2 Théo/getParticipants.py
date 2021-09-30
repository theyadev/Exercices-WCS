from er_eme import er_eme
def getParticipants():
    p = []
    new_p = None
    i = 1
    while new_p != "":
        new_p = input(
            f"\nComment la {i}{er_eme(i)} personne s'appelle-t-elle ? (Entrée pour finir) ")
        try:
            new_p = int(new_p)
            print('Nom invalide.\n\n')
            continue
        except:
            if len(new_p) == 0:
                pass
            elif len(new_p) < 3:
                print("Le nom doit contenir plus de 2 caractères!\n\n")
                pass
            else:
                p.append({
                    "name": new_p
                })
        i += 1

    return p