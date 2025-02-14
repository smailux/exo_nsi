def prochain_syracuse(u):
    if u % 2 == 0 :
        return u //2
    else :
        return u*3 + 1

def suite_syracuse(u):
    suite = [u]
    while u > 1 :
        u = prochain_syracuse(u)
        suite.append(u)
    return suite

def altitude_max(u):
    alt_max = u
    while u > 1 :
        u = prochain_syracuse(u)
        if u > alt_max :
            alt_max = u
        
    return alt_max

def duree_vol(u):
    return len(suite_syracuse(u))

def duree_vol2(u):
    duree = 0
    while u > 1 :
        u = prochain_syracuse(u)
        duree += 1
    return duree

def record_altitude(u_limite):
    a_record = 0
    u_record = 0
    for u in range(1, u_limite+ 1):
        a = altitude_max(u)
        if a > a_record :
            a_record = a
            u_record = u
    return {"u" : u_record, "a" : a_record}
    


    