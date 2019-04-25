from random import choice

def initialisation():
    grille = []
    for index in range(81):
        grille.append(0)
    return grille


def affiche(grille):

    for i in range(9):
        L=[]
        for j in range(9):
            L.append(grille[9*i+j])
        print(L)


def interdit_rangees(index, grille):
    interdit_ligne = {grille[index2] for index2 in range(81) if ((index2 // 9) == (index // 9)) and (grille[index2] != 0)}
    interdit_colon = {grille[index2] for index2 in range(81) if ((index2 % 9) == (index %9)) and (grille[index2] != 0)}
    interdit = interdit_ligne.union(interdit_colon)
    return interdit


def interdit_carre(index, grille):
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
    conflits = interdit_rangees(index, grille).union(interdit_carre(index, grille))
    if index == forbiden[0]:
        conflits = conflits.union({forbiden[1]})
    candidats = {1,2,3,4,5,6,7,8,9} - conflits
    return candidats


def add_element(grille, untrieds, index, candidats):
    grille[index] = choice(list(candidats))
    untrieds[index] -= {grille[index]}


def locate_min_candidats(grille, forbiden):
    minimum = 9
    index_min = 0
    for index in range(81):
        if grille[index] == 0:
            candidats = calcule_candidats(grille, index, forbiden)
            nb_candidats = len(candidats)
            if nb_candidats < minimum:
                minimum = nb_candidats
                index_min = index
    return minimum, index_min

def recursif_brut_solve(grille, forbiden = [0, 0]):
    try :
        index_case = grille.index(0)
        candidats = calcule_candidats(grille, index_case, forbiden )
        if not candidats:
            return False
        while candidats:
            valeur = choice(list(candidats))
            grille[index_case] = valeur
            if recursif_brut_solve(grille, forbiden):
                return True
            candidats -= {valeur}
        grille[index_case] = 0
        return False
    except :
        return True



def resolve(grille, forbiden = [0,0]):
    case_interdite = forbiden[0]
    valeur_interdite = forbiden[1]
    cases_vides = [index for index in range(81) if grille[index] == 0]
    untrieds = []
    nombre_de_cases = len(cases_vides)
    for index in range(81):
        untrieds.append({1,2,3,4,5,6,7,8,9})
    index = 0
    while index < nombre_de_cases:
        index_case = cases_vides[index]
        candidats = untrieds[index_case]-conflits(grille, index_case)
        if index_case == case_interdite:
            candidats -= {valeur_interdite}
        if candidats == set():
            if index == 0:
                return False
            else:
                untrieds[index_case] = {1,2,3,4,5,6,7,8,9}
                grille[index_case] = 0
            index = index-1
            untrieds[index_case] =untrieds[index_case]- {grille[index_case]}
        else:
            add_element(grille, untrieds, index_case, candidats)
            index += 1
    return True


def remove_random_element(grille):
    cases_pleines = fcases_pleines(grille)
    index = choice(cases_pleines)
    valeur = grille[index]
    grille[index] = 0
    return grille, index, valeur


def remove_safe_element(grille):
    grille1 = grille[:]
    grille1, index, valeur = remove_random_element(grille1)
    if recursif_brut_solve(grille1, [index, valeur]):
        return index, False
    else:
        return index, True


def remove1(grille):
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
    cases_pleines = [index for index in range(81) if grille[index] != 0]
    return cases_pleines


def affiche_candidats(grille):
    liste_candidats = []
    for index in range(81):
        liste_candidats.append(len(list({1,2,3,4,5,6,7,8,9} - set(calcule_candidats(grille, index)))))
    affiche(liste_candidats)


