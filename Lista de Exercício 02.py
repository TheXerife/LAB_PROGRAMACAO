# '''
# Exercícios sobre os comandos de condição em python

# '''
       
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.

def ex01():

    N1 = int(input("Digite um número: "))
    N2 = int(input("Digite outro número: "))
    result = (N1 + N2)

    if (result>10):

        print(f" \n O valor apresentado é maior que 10, a soma dos valores é {result}")

    else:

        print(f" \n O valor apresentado é menor que 10, mas a soma é {result}")

# Ex01()

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.

def ex02():

    N1 = int(input("Digite um número: "))
    N2 = int(input("Digite outro número: "))
    result = (N1 + N2)

    if (result>20):

        result = (result + 8)

        print(f" \n O valor apresentado é maior que 20, (a soma dos valores + 8) é {result}")

    elif (result <= 20):

        result = (result - 5)

        print(f" \n O valor apresentado é menor que 20, (a soma dos valores - 5) é {result}")


# ex02()

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".

def ex03():

    N1 = int(input("Digite um número: "))

    if (N1%3): 

        print("Não é múltiplo de 3")

    else:

        print("É múltiplo de 3!")

# ex03()

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.

def ex04():

    N1 = int(input("Digite um número: "))

    if (N1%5): 

        print("Não é divisível de 5")

    else:

        print("É divisível de 5!")

# ex04()

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

def ex05():

    N1 = int(input("Digite um número: "))

    if (N1%3) and (N1%7): 

        print("Não é divisível por 3 e por 7")

    else:

        print("É divisível por 3 e por 7!")

# ex05()       

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

def ex06():

    salario = float(input("Informe seu salário: "))
    prestacao = float(input("Quer pegar um emprestimo? informe o valor da prestação: "))

    ajuste = salario * 0.30

    if (prestacao > salario): 

        print("O emprestimo não poderá ser finalizado pois o valor da prestação é maior que seu salário!")

    elif (prestacao > ajuste):

        print(f"O emprestimo não poderá ser finalizado pois o valor ultrapaça 30% do seu salário!")

    elif (prestacao < ajuste):

        print(f"O emprestimo poderá ser finalizado. Não gasta tudo em cerveja!")


# ex06()

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.

def ex07():

    N1 = int(input("Digite um número: "))

    if (N1>20 and N1<50):

        print("O número está entre 20 e 50")

    else:

        print("O número não está entre 20 e 50")

# ex07()

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
        
def ex08():

    N1 = int(input("Digite um número: "))

    if (N1 < 20):

        print("O número é menor que 20")

    elif (N1 == 20):

        print("O número é igual a 20")

    elif (N1 > 20): 

        print("O número é maior que 20")    

# ex08()   

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
        
def ex09():

    D = (int(input("Digite o dia do seu nascimento (dd/--/----): ")))
    M = (int(input("Digite o mes do seu nascimento (--/mm/----): ")))
    A = (int(input("Digite o ano do seu nascimento (--/--/aaaa): ")))

    if (A >= 2024) or (A <= 1000):

        print("Data de nascimento inválida!")   

    elif (A > 1000):

        idade = float((((2024 - A)*365) - (M*30) - D)/365)

        print(f"Você tem {idade:.1f} anos!")


# ex09()


#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
        
def ex10():
        
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))       
    n3 = int(input("Digite outro número: ")) 

    lista = [n1, n2, n3]
    lista.sort()

    print(lista)


# ex10()    

#11. Faça um programa que leia 3 números e imprima o maior deles.
    
def ex11():
        
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))       
    n3 = int(input("Digite outro número: "))

    if (n1 > n2) and (n1 > n3):

        print(f"{n1} é o maior numero entre os 3 informado!")

    elif (n2 > n1) and (n2 > n3):

        print(f"{n2} é o maior numero entre os 3 informado!")

    elif (n3 > n1) and (n3 > n1):

        print(f"\n{n3} é o maior numero entre os 3 informado!")

# ex11()

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
        
def ex12():

    idade = int(input("Digite sua idade: "))

    if (idade > 65):

        print("Você tem mais de 65 anos!")

    elif (idade < 18):

        print("Você é menor de idade!")

    elif (idade > 18):

        print("Você é maior de idade!")

# ex12()    

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
        
def ex13():
        
    nome = str(input("Digite seu nome: "))
    n1 = float(input("Digite o valor de N1: "))
    n2 = float(input("Digite o valor de N2: "))

    lista = [nome, n1, n2]

    media = float((n1 + n2)/2)

    if (media >= 7):
        
        print(f"\n{lista} Média = {media:.2f} Aprovado!")

    else:
              
        print(f"\n{lista} Média = {media:.2f} Reprovado!")
 
# ex13()

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def ex14():

    salario = float(input("Digite seu salário (R$): "))

    if (salario < 600):

        print(f"\nVocê não tera desconto do INSS! ")

    elif (salario > 600) and (salario < 1200):

        desconto = (salario * 0.20)

        print(f"\nVocê tera 20% ou R${desconto} de desconto do INSS! ")

    elif (salario > 1200) and (salario < 2000):

        desconto = (salario * 0.25)

        print(f"\nVocê tera 25% ou R${desconto} de desconto do INSS! ")

    elif (salario > 2000):

        desconto = (salario * 0.30)

        print(f"\nVocê tera 30% ou R${desconto} de desconto do INSS! ")

# ex14()

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.


def ex15():

    compra = float(input("Digite o valor da sua compra (R$): "))

    if (compra < 20):

        valor = ((compra*0.45)+compra)

        print(f"\nSeu produto com 45% de lucro será R${valor}")

    elif (compra > 20):

        valor = ((compra*0.30)+compra)

        print(f"\nSeu produto com 30% de lucro será R${valor}")

# ex15()

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

def ex16():

    idade = int(input("Digite sua idade (xx): "))

    if (idade >= 5) and (idade <= 7):

        print("Infantil A")

    elif (idade >= 8) and (idade <= 10):

        print("Infantil B")

    elif (idade >= 11) and (idade <= 13):

        print("Juvenil A")

    elif (idade >= 14) and (idade <= 17):

        print("Juvenil B")

    elif (idade >= 100):

        print("Você não pode participar por ter mais de 100 anos!")        

    elif (idade >= 18): 

        print("Sênior")

    else:

        print("Digite um valor válido para as categorias! ")

# ex16()

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

def ex17():

    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade (xx): "))
    saldo = 100

    if (idade <= 10):
    
        valor = 30

    elif (idade > 10) and (idade <= 29):
    
        valor = 60
        saldo -= valor
        
    elif (idade > 29) and (idade <= 45):
    
        valor = 120

    elif (idade > 45) and (idade <= 59):
    
        valor = 150

    elif (idade > 59) and (idade <= 65):
    
        valor = 250

    elif (idade > 65):
    
        valor = 400

    print(f"{nome}, o valor do seu plano será {valor} e será descontado do seu saldo.")
    print(f"Seu saldo atual é {saldo}")

ex17()      


#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
        
def ex21():

    print ("Qual a data de hoje?")

    dia = int(input("Digite o dia de hoje (dd/xx/xxxx): "))
    mes = int(input("Digite o mes (xx/mm/xxxx): "))
    ano = int(input("Digite o ano (xx/xx/aaaa): "))

    livro = str(input("Digite o nome do livro: "))

    menu = """

    1 - Aluno
    2 - Professor

    """
    print (menu)

    escolha = int(input("Digite o tipo do usuário: "))

    if (escolha == 1):  
    
        print("Você é um aluno!")

        dia += 3 

        if (dia > 30):

            mes += 1
            dia -= 30

            if (mes > 12):

                ano += 1 
                mes -= 12

        print(f"Seu prazo de devolução é {dia}/{mes}/{ano}")
        
    elif (escolha == 2): 

        
        dia += 10

        if (dia > 30):

            mes += 1
            dia -= 30

            if (mes > 12):

                ano += 1 
                mes -= 12

        print("Você é um professor!")
        print(f"Seu prazo de devolução é {dia}/{mes}/{ano}")

    else:

        print("Digite um valor válido!")


# ex21()


#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal
        

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
    
# def ex24():
        
# LSN4149

#     placa = str(input("Digite sua placa: "))
#     print(placa)

#     placa.split()


# ex24()

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
