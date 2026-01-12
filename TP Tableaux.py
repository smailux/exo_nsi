from random import randint

tab_test = [2,5,-1,7, 3]

def ajoute(tab, a):
    for i in range(len(tab)):
        tab[i] += a


def affine(tab, m, p):
    for i in range(len(tab)):
        tab[i] = m * tab[i] + p

def remplacer(tab, a,b):
    for i in range(len(tab)):
        if tab[i] == a :
            tab[i] = b
            
def interverti(tab, a, b):
    for i in range(len(tab)):
        if tab[i] == a :
            tab[i] = b
        elif tab[i] == b :
            tab[i] = a
            
def normalise(tab, a,b): #a<b
    for i in range(len(tab)):
        if tab[i]> b:
            tab[i]= b
        elif tab[i]< a:
            tab[i] = a
            
def echange(tab,i,j):
    tab[i], tab[j] = tab[j], tab[i]
    
def melange(tab):
    for i in range(len(tab)):
        j = randint(0,i)
        tab[i], tab[j] = tab[j], tab[i]
        
def miroir(tab):
    for i in range(len(tab)//2):
        j = len(tab)-i-1
        tab[i], tab[j] = tab[j], tab[i]
        
def initialiser(m, n, val=0):
    tab = [0]*m
    for i in range(m):
        tab[i] = [val]*n
    return tab   
        
        
def initialiser2(m,n,val=0):
    return [[val]*n for i in range(m)]

def affichage_simple(tab):
    for t in tab :
        print(t)
        
def maximum(tab):
    maxi = tab[0][0]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] >= maxi:
                maxi = tab[i][j]
                max_i, max_j = i, j
    return (maxi, max_i, max_j)

def diagonale1(n):
    tab = initialiser(n,n)
    for i in range(n):
        tab[i][i] = 1
    return tab

def diagonale2(n):
    tab = initialiser(n,n)
    for i in range(n):
        tab[n-i-1][i] = 1
    return tab

def diagonales(n):
    tab = initialiser(n,n)
    for i in range(n):
        tab[i][i], tab[n-i-1][i] = 1, 1
    return tab

def que_col(n, k):
    tab = initialiser(n,n)
    for i in range(n):
        tab[i][k] = 1
    return tab

def que_col_paires(n):
    tab = initialiser(n,n)
    for i in range(n):
        for j in range(n):
            if j % 2 == 0 :
                tab[i][j] = 1
    return tab

def addition(n):
    tab = initialiser(n,n)
    for i in range(n):
        for j in range(n):
            tab[i][j] = i + j
    return tab

def damier(n):
    tab = initialiser(n,n)
    for i in range(n):
        for j in range(n):
            if (i +j) & 1 == 0:
                tab[i][j] = 1
            
    return tab


def transposer(tab):
    tab_i, tab_j = len(tab), len(tab[0])
    tab2 = initialiser(tab_j, tab_i)
    for j in range(tab_i):
        for i in range(tab_j):
            tab2[i][j] = tab[j][i]
    return tab2

def affichage_avance(tableau, label=""):
    maxi, _, _ = maximum(tableau)
    m = len(tableau)
    n = len(tableau[0])
    plus_grande_valeur = max(maxi, m-1, n-1)
    k = len(str(plus_grande_valeur))+1
    k2 = max(k, len(label))
    print(label.rjust(k2) + "|" +\
        "".join([str(i).rjust(k) for i in range(n)]))
    print("-"*k2 + "+" + "-"*(k*n))
    for i in range(m):
        ligne = str(i).rjust(k2)+"|"+\
            "".join([str(tableau[i][j]).rjust(k) for j in range(n)])
        print(ligne)
        
def table_addition(n):
    affichage_avance(addition(n))

def taille_max(tab):
    maxi, long_max = tab[0][0], len(str(tab[0][0]))
    for t in tab :
        for v in t :
            x= len(str(v))
            if x > long_max :
                maxi, long_max = v, x
    return(long_max)


def affichage_avance2(tableau, label=""):
    maxi, _, _ = maximum(tableau)
    m = len(tableau)
    n = len(tableau[0])
    k = taille_max(tableau)+1
    k2 = max(k, len(label))
    print(label.rjust(k2) + "|" +\
        "".join([str(i).rjust(k) for i in range(n)]))
    print("-"*k2 + "+" + "-"*(k*n))
    for i in range(m):
        ligne = str(i).rjust(k2)+"|"+\
            "".join([str(tableau[i][j]).rjust(k) for j in range(n)])
        print(ligne)


    
    
