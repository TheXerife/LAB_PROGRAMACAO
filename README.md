# LAB_PROGRAMACAO

Int: (Inteiro) # Aceita números inteiros positivos e negativos

Float: (Real) Aceita números inteiros e fracionados positivos e negativos

Str: (Texto) Aceita textos, símbolos, em branco, etc..

Bool: (Logico) Verdadeiro ou falso

_______________________________________________________________________________________

Atribuição e conversão de variáveis
Variável = Tipo (Atribuição)
print (f"{variável} {type(variável)}")

_______________________________________________________________________________________

Operador Logico
Not (não)
And (e)
Or (ou)

_______________________________________________________________________________________

Operador Aritmético
+ : Adição
- : Subitração
* : Multiplicação
/ : Divição
// : Divisão Inteira
% : Resto
** : Potenciação
_______________________________________________________________________________________

Operador Relacionais
A igual B {a == b}
A diferente de B {a != b}
A maior que B {a > b}
A maior ou igual B {a >= b}
A menor que B {a < b}
A menor ou igual B {a <= b}
_______________________________________________________________________________________

Operações matemáticas especiais
Import math
Sqrt: Raiz quadrada
Log: Logaritmo
Sin: Seno (Calculado em Radiano)
Cos: Cosseno (Calculado em Radiano)
Tan: Tangende (Calculado em Radiano)
Floor: Piso (Arredondar para baixo) Ex: 1,6 = 1
Ceil: Teto (Arrendondar para cima) Ex: 1,2 = 2
Factorial: Fatorial
_______________________________________________________________________________________

Estrutura Condicional

if (condição1):

# código a ser executado se a condição for verdadeira

    elif (condição2):

# código a ser executado se outra condição for verdadeira

else:

# código a ser executado se nenhuma das condições for verdadeira
_______________________________________________________________________________________

Estrutura de repetição (While - Enquanto)
While <condição> :
# código a ser executado se a condição for atendida
_______________________________________________________________________________________

Estrutura de repetição (For - Para)
For (variável) in range (x, y)
# código a ser executado de x até y vezes
_______________________________________________________________________________________

Listas em Python - Definida por colchetes [].

# Criação de Lista

lista = [1, 2, 3, 4, 5]

# Acesso a Elementos

primeiro_elemento = lista[0]
segundo_elemento = lista[1]

# Modificação de Elementos

lista[0] = 10

# Adição de Elementos

lista.append(6) # Adiciona 6 no final
lista.insert(2, 20) # Adiciona 20 na posição 2
lista.extend([7, 8, 9]) # Adiciona elementos da lista ao final

# Remoção de Elementos

lista.remove(4) # Remove o elemento 4
elemento_removido = lista.pop(1) # Remove e retorna o elemento na posição 1
del lista[2] # Remove o elemento na posição 2

# Operações com Listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
nova_lista = lista1 + lista2 # Concatenação de listas
lista_repetida = lista1 * 3 # Repetição de lista
_______________________________________________________________________________________

Tupla em Python - Definida por parênteses ().

# Criação de Tupla
tupla = (1, 2, 3, 4, 5)

# Acesso a Elementos
primeiro_elemento = tupla[0]
segundo_elemento = tupla[1]

# Operações Básicas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla = tupla1 + tupla2 # Concatenação de tuplas
repetida = tupla1 * 3 # Repetição de tupla

______________________________________________________________________________________
