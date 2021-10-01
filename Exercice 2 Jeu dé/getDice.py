def getDice():
    a = input("\n\nCombien de faces voulez vous pour le dé ? (max: 100) ")
    try:
        a = int(a)
        if a <= 100:
            return a
        else:
            print("Nombre trop grand!\n")
            return getDice() 
    except:
        print("Nombre invalide.\n")
        return getDice()