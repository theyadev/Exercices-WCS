from writeAnimation import writeAnimation
def showWinners(winners, max_number, old_winners, old_max_number):
    if winners and old_winners != None:
        if len(winners) == 1:
            writeAnimation(
                f"Le vainqueur de la derniere partie est: \033[33m{winners[0]}\033[0m avec un score de \033[92m{max_number}\033[0m\n\n")
        else:
            writeAnimation(
                f"Les vainqueurs de la derniere partie sont: \033[33m{', '.join(winners)}\033[0m avec un score de \033[92m{max_number}\033[0m\n\n")

        writeAnimation('Et voici les parties precedentes !\n\n')

        for index in range(len(old_winners)):
            if len(old_winners[index]) == 1:
                writeAnimation(
                    f"Vainqueur: \033[33m{old_winners[index][0]}\033[0m avec un score de \033[92m{old_max_number[index]}\033[0m\n\n")
            else:
                writeAnimation(
                    f"Vainqueurs: \033[33m{', '.join(old_winners[index])}\033[0m avec un score de \033[92m{old_max_number[index]}\033[0m\n\n")

