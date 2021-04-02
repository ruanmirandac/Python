# Listas

# Usamos os [] para a criação de listas

nome = ['Ruan', 'Ana', 'Angecra']

# Para acessar as listas, usamos o seu índice
# Uma lista sempre começa em 0 

print(nome)     # Mostra toda a lista
print(nome[0])  # Mostra o índice 0, no caso o nome 'Ruan'

# Podemos formatar um item de uma lista se for string

print(nome[2].upper())

for nomes in nome:
    print(nomes)