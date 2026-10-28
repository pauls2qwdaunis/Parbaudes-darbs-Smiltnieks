# ----------------------------------------------------------------------
# C1. Saraksta kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar sešiem skaitļiem. Izvadi to skaitu, summu, vidējo, lielāko un mazāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā skaitļus, nosauc ar vārdu vertibu_kopa.

saraksts = [3, 66, 12, 21, 7, 90]

skaits = len(saraksts)
summa = sum(saraksts)
vidējais = summa / skaits
lielākais = max(saraksts)
mazākais = min(saraksts)

print("saraksts:", saraksts)
print("skaits:", skaits)
print("summa:", summa)
print("vidējais:", vidējais)
print("lielākais:", lielākais)
print("mazākais:", mazākais)

