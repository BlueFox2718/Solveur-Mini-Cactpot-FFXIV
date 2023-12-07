from itertools import permutations

def genere_permutation(Tab):
    perm_list = list(permutations(Tab))
    return [list(perm) for perm in perm_list]

X = 1
Y = 2
Z = 3
T = 5
Nb_restants = [1,2,3,4,5,6,7,8,9]
Nb_restants.remove(X)
Nb_restants.remove(Y)
Nb_restants.remove(Z)
Nb_restants.remove(T)

TT = genere_permutation(Nb_restants)
Grilles = []
for e in TT:
    #print([X,e[0],Y,e[1],Z,e[2],T,e[3],e[4]])
    #Grilles += [[X,e[0],Y,e[1],Z,e[2],T,e[3],e[4]]] #Grille 1
    Grilles += [[X,Y,Z,e[0],T,e[1],e[2],e[3],e[4]]] #Grille 2

Prix = [[6, 10000],[7, 36],[8, 720],[9, 360],[10, 80],[11, 252],[12, 108],[13, 72],[14, 54],[15, 180],[16, 72],[17, 180],[18, 119],[19, 36],[20, 306],[21, 1080],[22, 144],[23, 1800],[24, 3600]]
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
print("L1 : ",Moyenne_L1)
print("L2 : ",Moyenne_L2)
print("L3 : ",Moyenne_L3)
print("C1 : ",Moyenne_C1)
print("C2 : ",Moyenne_C2)
print("C3 : ",Moyenne_C3)
print("D1 : ",Moyenne_D1)
print("D2 : ",Moyenne_D2)