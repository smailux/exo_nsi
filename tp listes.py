from math import *
def maximum(nombres):
    pg = nombres[0]
    for v in nombres :
        print(v)
        if v > pg :
            pg = v
    return pg

def moyenne(valeurs):
    somme, cpt = 0, 0
    for i in valeurs :
        somme += i
        cpt += 1
    return somme/cpt

def moyenne_ponderee(valeurs, coeff):
    eff, somme = 0, 0
    for i in range(len(valeurs)):
        somme += valeurs[i] * coeff[i]
        eff += coeff[i]
    return somme/eff

def position_max(liste):
    pg = liste[0]
    imax = 0
    for i in range(len(liste)) :
        if liste[i] > pg :
            pg = liste[i]
            imax = i
    return imax
    
def addition(l1, l2):
    assert len(l1) == len(l2)
    resultat = [0]*len(l1)
    for i in range(len(l1)):
        resultat[i] = l1[i]+l2[i]
    return resultat


def alterner(l1, l2):
    assert len(l1) == len(l2)
    resultat = []
    for i in range(len(l1)):
        if i % 2 == 0 :
            resultat.append(l1[i])
            resultat.append(l2[i])
        else :
            resultat.append(l2[i])
            resultat.append(l1[i])
    return resultat

def egales(l1, l2):
    assert len(l1) == len(l2)
    for i in range(len(l1)):
        if l1[i] == l2[i] :
            resultat = True
        else :
            return False      
    return True

def selection(l1, l2, l3):
    assert len(l1) == len(l2) and len(l1) == len(l3)
    resultat = []
    for i in range(len(l1)):
        if l3[i] > 0 :
            resultat.append(l1[i])
        elif l3[i] < 0 :
            resultat.append(l2[i])
        else :
            resultat.append(0)
    return resultat
            
            
            
def liste_speciale(n):
    resultat = []
    for i in range(n):
        resultat.append(1)
        resultat.append(i+1)
    return resultat

def liste_speciale2(n):
    resultat = []
    for i in range(n):
        resultat.extend(range(1, i+2))
        
    return resultat
        
def premiers_premiers(n): 
    nb_prem = [2]
    for i in range(3, n, 2):
        isPrem = True
        for d in range(2, int(sqrt(i))+1):
            if i%d == 0 :
                isPrem = False
                break
                
        if isPrem:
            nb_prem.append(i)
            
                
    return nb_prem


    
            