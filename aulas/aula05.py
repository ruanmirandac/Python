# Formatação de String

nome = input('Digite o sue nome: ')
print(f'Olá, {nome:10}, seja bem-vindo!')
print('='*50)

# Usamos : após a variavel para poder fazer formatação

print(f'Olá, {nome:>10}, seja bem-vindo!') # > Alinha a direita
print('='*50)
print(f'Olá, {nome:<10}, seja bem-vindo!') # > Alinha a esquerda
print('='*50)
print(f'Olá, {nome:^10}, seja bem-vindo!') # ^ Alinha ao centro
print('='*50)
print(f'Olá, {nome:•^10}, seja bem-vindo!') # ^ Alinha ao centro com o sinal • em volta
print('='*50)

# Formantando Ponto Flutuante

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor:'))
print(f'A potência dos valores é {n1**n2:.2f}')

# :.2f = onde 2 indica o numero de casas decimais após a virgula

# Quebra de Linha e Tabulação

# \n - quebra linha
# \t - tabulação
# end='' - dentro de um print faz com que a linha não seja quebrada