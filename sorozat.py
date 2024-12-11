import random

def lszamok():
    szamok=[random.randint(1,99) for _ in range(5)]
    return szamok
def egyjegyu(szamok):
    return sum(1 for szam in szamok if szam <10)

def kiir(szamok, egyjegyu):
    print("II/A, B, C:")
    print("; ".join(map(str, szamok)))
    print("II/D, E:")
    print(f"Az egyjegyűek száma: {egyjegyu}.")
    
def file_kiir(egyjegyuek, fajlnev="szamok.txt"):
    with open(fajlnev, "w") as fajl:
        fajl.write("II/F:")
        fajl.write(f"Az egyjegyűek száma: {egyjegyuek}.")