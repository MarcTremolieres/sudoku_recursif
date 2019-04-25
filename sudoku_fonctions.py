from random import choice

def initialisation():
    #Ecrit des 0 dans toute la grille
    grille = []
    for index in range(81):
        grille.append(0)
    return grille


def affiche(grille):
    #Affiche sous fore de grille
    for i in range(9):
        L=[]
        for j in range(9):
            L.append(grille[9*i+j])
        print(L)


def interdit_rangees(index, grille):
    #Renvoie les nombres des rangées de la case
    interdit_ligne = {grille[index2] for index2 in range(81) if (index2 // 9) == (index // 9)}
    interdit_colon = {grille[index2] for index2 in range(81) if (index2 % 9) == (index %9)}
    interdit = interdit_ligne.union(interdit_colon)
    return interdit


def interdit_carre(index, grille):
    #Renvoie les nombre du petit carré de la case
    ligne = index // 9
    colon = index % 9
    ligne_carre = ligne // 3
    colon_carre = colon // 3
    interdit =[]
    for index2 in range(81):
        ligne2 = index2 // 9
        colon2 = index2 % 9
        ligne_carre2 = ligne2 // 3
        colon_carre2 = colon2 // 3
        if grille[index2] != 0:
            if (ligne_carre2 == ligne_carre) and (colon_carre2 == colon_carre):
                interdit.append(grille[index2])
    return interdit


def calcule_candidats(grille, index, forbiden):
    #Renvoie l'ensemble des candidats d'une case donnée de la grille
    conflits = interdit_rangees(index, grille).union(interdit_carre(index, grille))
    if index == forbiden[0]:
        conflits = conflits.union({forbiden[1]})
    candidats = {1,2,3,4,5,6,7,8,9} - conflits
    return candidats


def recursif_brut_solve(grille, forbiden = [0, 0]):
    #Renvoie True et la grille résolue, ou bien False et la grille initiale
    try :
        index_case = grille.index(0)  #Si erreur c'est que la grille est résolue ( aucun 0)
        candidats = calcule_candidats(grille, index_case, forbiden )
        if not candidats:
            return False    #Grille impossible
        while candidats:
            valeur = choice(list(candidats))
            grille[index_case] = valeur
            if recursif_brut_solve(grille, forbiden):
                return True #On a trouvé une solution
            candidats -= {valeur}  #On épuise les candidats
        grille[index_case] = 0  #Plus de candidat : on revient en arrière en remettant la grille dans l'état initial
        return False
    except :
        return True



def remove_random_element(grille):
    #Supprime une case pleine au hasard
    cases_pleines = fcases_pleines(grille)
    index = choice(cases_pleines)
    valeur = grille[index]
    grille[index] = 0
    return index, valeur


def remove_safe_element(grille):
    #Supprime un élément et résoud sans le remettre à sa place.
    #Si c'est impossible alors la solution est encore unique
    grille1 = grille[:]
    index, valeur = remove_random_element(grille1)
    if recursif_brut_solve(grille1, [index, valeur]):
        return index, False
    else:
        return index, True


def remove1(grille):
    #Essaye de supprimer un élément en conservant une solution unique
    #Continue jusqu'à épuisement des candidats.
    not_removed = []
    cases_pleines = fcases_pleines(grille)
    while set(cases_pleines) != set(not_removed):
        index, reussite = remove_safe_element(grille)
        if reussite:
            return index, True
        else:
            not_removed.append(index)
    return index, False


def fcases_pleines(grille):
    #Renvoie la liste des cases pleines
    cases_pleines = [index for index in range(81) if grille[index] != 0]
    return cases_pleines




