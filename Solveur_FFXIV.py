# ==================================================== #
# Code écrit par Mathieu Cima 2023                     #
# Dans le cadre de la vidéo YouTube ci jointe:         #
# https://www.youtube.com/watch?v=Mnl7zBY1TGc          #
# code source et algorithme libre de droit             #
# Paternité intelectuel de l'algorithme à Mathieu Cima #
# Tout usage à des fins commerciales est interdit      #
# ==================================================== #

from itertools import permutations

def genere_permutation(Tab):
    perm_list = list(permutations(Tab))
    return [list(perm) for perm in perm_list]

def main():
    # === SAISIE DE LA GRILLE ===
    grille = [0,0,0,0,0,0,0,0,0]
    configuration = 'none'
    print("Voici la numérotation de la grille")
    for i in range(3):
        print(3*i,'|',3*i+1,'|',3*i+2)
    print("Saisir la position de la case révélée")
    position_case_1 = int(input(""))
    print("Saisir la valeur de la case révélée")
    valeure_case_1 = int(input(""))
    grille[position_case_1] = valeure_case_1
    if valeure_case_1 > 9 or valeure_case_1 < 1 :
        print("Erreur valeur")
        return 1
    if position_case_1 in [0,2,4,6]:
        configuration = 'parfait'
        case_a_jouer = [0,2,4,6]
        case_a_jouer.remove(position_case_1)
        for c in case_a_jouer:
            print("Jouer et saisir valeur de la case",c)
            grille[c] = int(input(""))
    if position_case_1 == 8:
        configuration = 'parfait_r'
        case_a_jouer = [2,4,6]
        for c in case_a_jouer:
            print("Jouer et saisir valeur de la case",c)
            grille[c] = int(input(""))
    if position_case_1 in [1,7]:
        configuration = 'second'
        case_a_jouer = [position_case_1-1,position_case_1+1,4]
        for c in case_a_jouer:
            print("Jouer et saisir valeur de la case",c)
            grille[c] = int(input(""))
    if position_case_1 in [3,5]:
        configuration = 'second'
        case_a_jouer = [position_case_1-3,position_case_1+3,4]
        for c in case_a_jouer:
            print("Jouer et saisir valeur de la case",c)
            grille[c] = int(input(""))
    print("Voici la grille actuellement")
    for i in range(3):
        print(grille[3*i],'|',grille[3*i+1],'|',grille[3*i+2])
    valeur_saisies = [val for val in grille if val != 0]
    if (len(valeur_saisies) != 4) or (len(valeur_saisies) != len(set(valeur_saisies))) or (not all(0 < val < 10 for val in valeur_saisies)):
        if (len(valeur_saisies) != 4) : print("Erreur de saisie de grille: valeur nulle entrée")
        if (len(valeur_saisies) != len(set(valeur_saisies))) : print("Erreur de saisie de grille: valeur nulle entrée ou même valeur entrée plusieurs fois")
        if (not all(1 < val < 9 for val in valeur_saisies)) : print("Erreur de saisie de grille: valeaur non comprise entre 1 et 9 entrée")
        return 1
    # === CALCUL LES DIFFERENTES GRILLES ===
    Nb_restants = [1,2,3,4,5,6,7,8,9]
    Nb_restants.remove(valeur_saisies[0])
    Nb_restants.remove(valeur_saisies[1])
    Nb_restants.remove(valeur_saisies[2])
    Nb_restants.remove(valeur_saisies[3])
    TT = genere_permutation(Nb_restants)
    Grilles = []
    for e in TT:
        Grille_a_ajouter = [0,0,0,0,0,0,0,0,0]
        count = 0
        for i in range(9):
            if grille[i] == 0:
                Grille_a_ajouter[i] = e[count]
                count += 1
            else:
                Grille_a_ajouter[i] = grille[i]
        Grilles += [Grille_a_ajouter]
    # === CALCUL LES MOYENNES ===
    Prix_classe = [-1,-1,-1,-1,-1,-1,10000,36,720,360,80,252,108,72,54,180,72,180,119,36,306,1080,144,1800,3600]
    Moyenne_L1 = 0
    Moyenne_L2 = 0
    Moyenne_L3 = 0
    Moyenne_C1 = 0
    Moyenne_C2 = 0
    Moyenne_C3 = 0
    Moyenne_D1 = 0
    Moyenne_D2 = 0
    for g in Grilles:
        Moyenne_L1 += Prix_classe[g[0]+g[1]+g[2]]
        Moyenne_L2 += Prix_classe[g[3]+g[4]+g[5]]
        Moyenne_L3 += Prix_classe[g[6]+g[7]+g[8]]
        Moyenne_C1 += Prix_classe[g[0]+g[3]+g[6]]
        Moyenne_C2 += Prix_classe[g[1]+g[4]+g[7]]
        Moyenne_C3 += Prix_classe[g[2]+g[5]+g[8]]
        Moyenne_D1 += Prix_classe[g[0]+g[4]+g[8]]
        Moyenne_D2 += Prix_classe[g[2]+g[4]+g[6]]
    Moyenne_L1 = Moyenne_L1/120.0
    Moyenne_L2 = Moyenne_L2/120.0
    Moyenne_L3 = Moyenne_L3/120.0
    Moyenne_C1 = Moyenne_C1/120.0
    Moyenne_C2 = Moyenne_C2/120.0
    Moyenne_C3 = Moyenne_C3/120.0
    Moyenne_D1 = Moyenne_D1/120.0
    Moyenne_D2 = Moyenne_D2/120.0
    print("Ligne 0-1-2 : ",Moyenne_L1)
    print("Ligne 3-4-5 : ",Moyenne_L2)
    print("Ligne 6-7-8 : ",Moyenne_L3)
    print("Colonne 0-3-6 : ",Moyenne_C1)
    print("Colonne 1-4-7 : ",Moyenne_C2)
    print("Colonne 2-5-8 : ",Moyenne_C3)
    print("Diagonale 0-4-8 : ",Moyenne_D1)
    print("Diagonale 2-4-6 : ",Moyenne_D2)
    Tab_allignement = [Moyenne_L1,Moyenne_L2,Moyenne_L3,Moyenne_C1,Moyenne_C2,Moyenne_C3,Moyenne_D1,Moyenne_D2]
    maximum = max(Tab_allignement)
    print("Conclusion : Il faut jouer cette configuration pour un gain moyen de",maximum,"PGS")
    if maximum == Moyenne_L1:
        print("X|X|X")
        print("0|0|0")
        print("0|0|0")
    if maximum == Moyenne_L2:
        print("0|0|0")
        print("X|X|X")
        print("0|0|0")
    if maximum == Moyenne_L3:
        print("0|0|0")
        print("0|0|0")
        print("X|X|X")
    if maximum == Moyenne_C1:
        print("X|0|0")
        print("X|0|0")
        print("X|0|0")
    if maximum == Moyenne_C2:
        print("0|X|0")
        print("0|X|0")
        print("0|X|0")
    if maximum == Moyenne_C3:
        print("0|0|X")
        print("0|0|X")
        print("0|0|X")
    if maximum == Moyenne_D1:
        print("X|0|0")
        print("0|X|0")
        print("0|0|X")
    if maximum == Moyenne_D2:
        print("0|0|X")
        print("0|X|0")
        print("X|0|0")
    print("Programme et algorithme conçu par Mathieu Cima - 2023. Open Source. Tout usage à des fins commerciales est interdit")
    

main()
