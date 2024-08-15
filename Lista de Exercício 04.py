import random
import math

'''
Lista de Exercícios referentes a coleções em python

'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".

def ex01():

    lista = []

    for _ in range (10):

        lista.append(random.randrange(100))
        lista.sort()

    print(lista)

    busca = int(input("\nDigite o numero de busca: "))

    if busca in lista:

        posicao = lista.index(busca)
        vezes = lista.count(busca)

        print(f"\nO numero {busca} foi localizado na posição {posicao+1}")
        print(f"Ele apareceu {vezes} vezes\n")

    else:

        print(f"\nO numero  {busca} não foi localizado!\n")



#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.

def ex02():

    lista = []

    for i in range (10):

        # letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # letra = random.choice(letras)

        lista.append(chr(random.randrange(65,91)))
        print (f"{i+1}° - {lista[i]}")

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.

def ex03():

    lista = []

    for i in range (15):

        numero = random.randrange(100)

        if (numero%2 == 0):

            print (f"{i+1}° - {numero} (Par)")

        else:

            print (f"{i+1}° - {numero} - (Impar)")

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.

def ex04():

    lista = []

    for _ in range (8):

        numero = random.randrange(100)
        lista.append(numero)

        if (numero%6 == 0):

            print(f"{numero} é multiplo de 6")
    
    print(lista)

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.

def ex05():

    avaliacao = []

    for _ in range (2):

        nome = str(input("Digite um nome: "))
        n1 = random.randrange(11)
        n2 = random.randrange(11)
        media = ((n1 + n2) / 2)

        if (media > 7):

            situacao = "Aprovado"

            aluno = (f"""{nome}  N1: {n1}  N2: {n2} - Média: {media} - {situacao}""")

            avaliacao.append(aluno)

        else: 

            situacao = "Reprovado"

            aluno = (f"{nome} - N1: {n1}  N2: {n2} - Média: {media} - {situacao}")

            avaliacao.append(aluno)


    for _ in avaliacao:

        print(_)


#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.

def ex06():

    funcionarios = []

    for i in range (20):

        reajuste = 0
        salario = random.randrange(1000,3000)
        reajuste = salario + (salario * 0.08) 

        funcionario = (f"{i+1}º - Salário: R${salario} - Salário ajustado: R${reajuste}") 

        funcionarios.append(funcionario)

    for funcionario in funcionarios:

        print(funcionario)

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%

def ex07():

    itens = []

    for _ in range(100):

        item = {}

        codigo = random.randrange(100000,1000000)
        preco_compra = random.randrange(1,100)
        preco_venda = random.randrange(preco_compra) + preco_compra + 1 

        item["Codigo"] = codigo
        item["Custo"] = preco_compra
        item["Venda"] = preco_venda

        itens.append(item)

    for item in itens:

        print(item)

    print("\nProdutos e seus Lucros:\n")

    acima = 0 
    media = 0
    baixo = 0

    for item in itens:

        custo = item["Custo"]
        venda = item["Venda"]

        lucro = venda - custo
        porcentagem = (lucro/custo) * 100

        print(f"{item["Codigo"]} - Lucro: (R${lucro},00 ou {porcentagem:.2f}%)")

        if porcentagem > 20:
            acima += 1

        elif porcentagem > 10 and porcentagem < 20:
            media += 1 

        elif porcentagem < 10:
            baixo += 1

    menu = f"""
Acima de 20%: {acima}
Entre 10% e 20%: {media}
Abaixo de 10%: {baixo}
    """

    print(menu)
       
#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.


def ex08():

    
    itens = []

    for _ in range(30):

        item = {}

        codigo = random.randrange(100000,1000000)
        preco_compra = random.randrange(1,100)
        preco_venda = random.randrange(preco_compra) + preco_compra

        item["Codigo"] = codigo
        item["Custo"] = preco_compra
        item["Venda"] = preco_venda

        itens.append(item)

    
    #Caso queria todos os itens da lista:

    for item in itens:

        print(item)

    busca = int(input("Digite o codigo a ser localizado: "))

    encontrado = False

    for item in itens:

        if item["Codigo"] == busca:

            print("Código localizado!")
            
            encontrado = True

            break

    if encontrado == False:

        print("Código não localizado!")
      
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

def ex09():

    def usando_lista():

        conjunto1 = []
        conjunto2 = []

        for _ in range (10):

            conjunto1.append(random.randrange(100))

        print(conjunto1)

        for _ in range (10):

            conjunto2.append(random.randrange(100))

        print(conjunto2)

        conjunto1 = set(conjunto1)
        conjunto2 = set(conjunto2)

        repetidos = conjunto1 & conjunto2

        print(repetidos)

    def usando_conjunto():

        conjunto1 = set()
        conjunto2 = set()

        while len(conjunto1) < 10:

            numero = random.randrange(20)
            conjunto1.add(numero)

        while len(conjunto2) < 10:

            numero = random.randrange(20)
            conjunto2.add(numero)
        
        print(conjunto1)
        print(conjunto2)

        repetido = conjunto1 & conjunto2

        print(f" Numeros repetidos: {repetido}")

    # usando_lista()
    # usando_conjunto()

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

def ex10():

    lista = []
    lista_fac = []
    media_lista = 0

    for item in range (10):

        lista.append(random.randrange(10))
        media_lista += item

    lista = sorted(lista)
    print(lista)

    maior = 0
    menor = 1000000
    pares = 0
   
    media_fac = 0

    for item in lista:

        item = math.factorial(item)

        lista_fac.append(item)

        media_fac += item

        if item > maior:

            maior = item 

        if item < menor:

            menor = item

        if (item % 2 == 0):

            pares += 1 

    lista_fac = sorted(lista_fac)

    print(lista_fac)

    percentual = (pares/10) * 100

    menu = f"""
Maior: {maior}
Menor: {menor}
Pares: {pares} - {percentual}%
Media dos Inicial: {media_lista}
Média dos Fatorial: {media_fac}   
    """

    print(menu)


#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

def ex11():
    
    numeros = []
    maior = 0
    menor = 100000
    par = 0
    media = 0
    
    for numero in range (10): 
        
        numero = random.randrange(1000)
        numeros.append(numero)
        numeros_ord = sorted(numeros)
        media += numero
        
        if (numero > maior):
            
            maior = numero
            
        elif (numero < menor):
            
            menor = numero
            
        if (numero % 2 == 0):
            
            par += 1
            
    pares = par/10 * 100
            
    menu = f"""
    
    {numeros}
    {numeros_ord}
    
    Maior: {maior}
    Menor: {menor}
    Porcentagem dos numeros pares: {pares}%
    Média: {media}

    """
    
    print(menu)

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

def ex14():
    
    numeros = []
    quad_numeros = []
    
    for numero in range (10):
        
        numero = random.randrange(10,100)
        
        numeros.append(numero)
        
    numeros = sorted(numeros)
    
    print(f"\n Lista 01\n \n {numeros}")    
    
    
    
    for numero in numeros:
        
        numero = numero * numero
        
        quad_numeros.append(numero)
        
    quad_numeros = sorted(quad_numeros)

        
    print(f"\n Lista 02 - quadrado da numero acima\n \n {quad_numeros}\n")      
        
    
ex14()

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias
