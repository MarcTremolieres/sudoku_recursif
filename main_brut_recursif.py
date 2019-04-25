from sudoku_fonctions import initialisation, remove1, fcases_pleines, affiche, recursif_brut_solve



grille = initialisation()
result = recursif_brut_solve(grille)
grille1 = grille[:]
print()
entree = ""
while entree != "exit" and entree != "quit":
    if entree == "r":
        index, reussite = remove1(grille1)
        if reussite:
            grille1[index] = 0
            print("Case ", index, " effaçée")
            affiche(grille1)
            print(len(fcases_pleines(grille1)), "cases pleines")
        else:
            print("Impossible")
    elif entree == "s":
        if recursif_brut_solve(grille1):
            print("ok")
            affiche(grille1)
            print(len(fcases_pleines(grille1)), "cases pleines")
        else:
            print("Impossible")
    else:
        affiche(grille)
        print(len(fcases_pleines(grille1)), "cases pleines")
        print()
        print("Entrez r pour remove , s pour solve, p pour afficher et  exit pour quitter")
    entree = input()
