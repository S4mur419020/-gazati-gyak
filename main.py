import bevezetes
import sorozat
import autom

print("I/A:")
nev, ev = bevezetes.A()
print("I/B:")
bevezetes.B(nev, ev)

szamok = sorozat.lszamok()
egyjegyuek = sorozat.egyjegyu(szamok)
sorozat.kiir(szamok, egyjegyuek)
sorozat.file_kiir(egyjegyuek)

autok = autom.beolvas("auto.txt")
print("III/Flotta:")
print(f"Autók száma: {autom.flotta(autok)}.")

legfiatalabb_auto = autom.legfiatalabb(autok)
print("III/Legfiatalabb:")
print(f"A legfiatalabb autó: {legfiatalabb_auto.nev} ({legfiatalabb_auto.gyartasi_ev}).")

atlag_kor = autom.atlagos_kor(autok)
print("III/Átlag kor:")
print(f"Az autók átlagos kora: {atlag_kor:.2f} év.")