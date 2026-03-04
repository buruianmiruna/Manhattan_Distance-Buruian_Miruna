#import functii din manhattan.py
from manhattan import manhattan_manual, manhattan_scipy

def citeste_vectori_din_fisier(fisier):
    #functie care citeste doi vectori dintr un fis text
    #deschidem fis in modul citire si citim pe rand liniile si le transf in liste de nr intregi
    with open(fisier, "r") as f:
        v1 = list(map(int, f.readline().split()))
        v2 = list(map(int, f.readline().split()))
    #return vectorii cititi
    return v1, v2

#acest bloc se executa doar daca rulam direct fis main.py
if __name__ == "__main__":
    #citim vectorii din fisier
    x, y = citeste_vectori_din_fisier("input.txt")
    #calc dist Man folosind metoda manuala
    d1 = manhattan_manual(x, y)
    #calc dist Man folosind scipy
    d2 = manhattan_scipy(x, y)
    #calc dist Man folosind scipy
    #afisam vectorii si distantele(cea calc manual+cu scipy)
    print("Vector X:", x)
    print("Vector Y:", y)
    print("Distanța Manhattan (manual):", d1)
    print("Distanța Manhattan (scipy):", d2)