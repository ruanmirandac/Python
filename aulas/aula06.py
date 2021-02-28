# Curso Python #06 - Tipos Primitivos e Saída de Dados

# int - número inteiros
# float - números com ponto flutuante
# boll - número booleano (True ou False)
# str - string / caracteres

n1 = int(input('Digite um numero: '))
print(type(n1))

# comando type(var) - mostra o tipo de variavel que estamos utilizando

n = input('Digite algo: ')
print(n.isnumeric())

# var.isnumeric() - retorna True para caso seja possivel converter a variavel em int

n = input('Digite algo: ')
print(n.isalpha())

# var.isalpha() - retorna True para caso seja uma string / letra

n = input('Digite algo: ')
print(n.isalnum())

# var.isalnum() - retorna True para caso seja alfa-numérico