# Usando métodos na String

name = 'ada lovelace'

print(name.title()) # var.title() - Primeira letra de cada nome em maiusculo

print(name.upper()) # var.upper() - Tranforma todas as letras em maiusculo

print(name.lower()) # var.lower() - Transforma todas as letras em minusculo

# Concatenação

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

print(f'Hello, {full_name.title()}!')

# Tabulação e Quebra de Linha

print('Python\nC\nJavaScrip') # Usamos \n para fazer uma quebra de linha

print('\tPython\n\tC\n\tJavaScrip') # Usamos \t para fazer uma tabulação

# Removendo Espaços em Branco de uma String
# A remoção é temporária, para ser permanente devemos passar o resultado do rstrip ou lstrip para dentro da variavél novamente

py = 'Python '
py1 = ' Python'
py2 = ' Python '
print(py.rstrip())  # var.rstrip() - Elimina o espaço em branco da direita
print(py1.lstrip()) # var.lstrip() - Elimina o espaço em branco da esquerda
print(py2.strip())  # var.strip()  - Elimina os espaços em brando da esquerda e direita

