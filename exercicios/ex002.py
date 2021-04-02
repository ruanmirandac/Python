# Soma dos termos de uma PA
# Formula: S = (a1 + an).n / 2

pa =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n= len(pa)
print(pa, n)

somapa = ((pa[0] + pa[-1]) * n) / 2
print(somapa)


