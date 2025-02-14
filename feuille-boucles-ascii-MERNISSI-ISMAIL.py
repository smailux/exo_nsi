def carre(n):
    for i in range(n):
        print("@"*n)

def triangle1(n):
    for i in range(n):
        print("@"*(i+1))

def diagonale1(n):
    for i in range(n):
        print(" "*i+ "\\")

def triangle2(n):
    for i in range(n):
        print(" "*i + "@"*(n-i))
        
def triangle3(n):
    for i in range(n):
        print("@"*(n-i))

def triangle4(n):
    for i in range(n):
        print(" " * (n-i) + "@" * (i+1))
        
def diagonale2(n):
    for i in range (n):
        print(" "* (n-i) + "/")
        
def motif1(n):
    for i in range(n):
        print("|" * i + "/" + "-" * (n-i-1))
def motif2(n):
    for i in range(n):
        print("|" * (n-i-1) + "\\" + "-" * i )

def motif3(n):
    for i in range(n):
        print("|" * i + "/" + "-" * ((n-i -1) *2) + "\\" + "|" * i)
    for i in range(n-1, -1, -1):
        print("|" * i + "\\" + "-" * ((n-i -1) *2) + "/" + "|" * i)

def pyramide(n):
    for i in range(n):
        print(" " * (n-i) + "@" * (i*2+1) + " " * (n-i))
        
def losange(n):
    pyramide(n)
    for i in range(2, n+1):
        print(" " * (i) + "@" * ((n-i)*2+1) + " " * (i))
    
    
        

        
        