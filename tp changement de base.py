alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def conversion(nb, b):
    res = ""
    while nb != 0 :
        res = alphabet[nb % b] + res
        nb = nb//b
    return res

def deconversion(nb, b):
    res = 0
    for chiffre in nb :
        res = res * b + alphabet.index(chiffre)
    return res

def conversion2(nb, b):
    puiss = 0
    while b ** puiss <= nb :
        puiss += 1
    res = ""
    while puiss != 0 :
        chiffre = nb // (b**(puiss-1)) 
        res = res + alphabet[nb// (b**(puiss-1))]
        nb = nb % (b**(puiss-1))
        puiss -= 1
    return res

def dconversion2(nb, b):
    res = 0
    puiss = 0
    for i in range(len(nb)-1, -1, -1) :
        chiffre = alphabet.index(nb[i])
        res = res + chiffre* (b** puiss)
        puiss += 1
    return res

def conversionk(nb, b, k=0):
    res = ""
    while nb != 0 :
        res = alphabet[nb % b] + res
        nb = nb//b
    if k > 0 :
        if k - len(res) > 0 :
            res.rjust(k, '0')
        else:
            res = res[(k-len(res)):]
    return res
        
        













def indices_maxi(tab):
    maximum = tab[0]
    indice = 0
    liste_indices = [indice]
    for i in range(len(tab)):
        if maximum < tab[i] :
            maximum = tab[i]
            liste_indices = [i]
            
        elif maximum == tab[i]:
            liste_indices.append[i]
    return maximum, liste_indices