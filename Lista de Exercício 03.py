print ('Funciona!!!')

import random
import math

#1.Faça um programa que imprima todos os números de 1 até 100.

def ex01():

    for numero in range(100): print(numero)

#2. Faça um programa que imprima todos os números pares de 100 até 1.

def ex02():

    for numero in range(100):

        if (numero % 2): pass

        else:print(_)

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.

def ex03():

    for numero in range(500):

        if (numero % 5 == 0): print(numero)

#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.

def ex04():

    for _ in range(20):

        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))

        menu_sexo = """

        1 - Masculino
        2 - Feminino

        """

        print(menu_sexo)
        sexo = int(input("Escolha a opção que você se identifica: "))

        if sexo == 1:

            if (idade > 21):

                sexo = "Masculino"

                print(f"Você tem {idade} anos e é do sexo {sexo}")

        elif sexo == 2: sexo = "Feminino"

        else: print("Digite um valor valido!")

#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.

def ex05():

    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))

    soma = 0

    for _ in range(10):
    # while (soma < 500):

        soma += n1 + n2

        print(soma)

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.

# def ex06():




#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.

def ex07():

    alunos = {}

    for _ in range(3):

        nome = str(input("\nDigite seu nome: "))
        n1 = int(input("Digite a nota da prova 1: "))
        n2 = int(input("Digite a nota da prova 2: "))
        media = ((n1 + n2) / 2)

        if (media >= 7):

            final = "Aprovado(a)!"

        else:

            final = "Reprovado(a)!"

        alunos[nome] = [n1, n2, media, final]

    for nome, info in alunos.items():

        n1, n2, media, final = info

        aluno_str = f"""
        Aluno: {nome}
        Nota 1: {n1}
        Nota 2: {n2}
        Média: {media} - {final}
        """

        print(aluno_str)

#8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto

def ex08():

    lista = {}

    for _ in range(10):

        nome = str(input("Digite seu nome: "))
        salario = random.randrange(3000)

        lista[nome] = salario

    for nome, salario in lista.items():

        lista_completa = f"""
        Nome: {nome}
        Salário: R${salario},00
        """

        print(lista_completa)

#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.

def ex09():

    bom = 0
    regular = 0
    media_idade = 0

    for _ in range(200):

        opniao = random.randrange(1,3)
        idade = random.randrange(50)
        media_idade += idade

        # 1 = Bom
        # 2 = Regular

        if (opniao == 1):

            bom += 1

        elif (opniao == 2):

            regular += 1

    qtd_pessoas = bom + regular

    relatorio = f"""

    {qtd_pessoas} Votos computados foram computados no sistema

    A idade média das pessoas é de {media_idade/qtd_pessoas} anos.

    {bom} votaram que o filme foi bom.
    {regular} votaram que o filme foi regular.

    """

    print(relatorio)

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.




#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.

def ex11():

    cont = 0
    valores = 0

    for _ in range(500):

        numero = random.randrange(500)
        valores += 1

        if (numero == 0):

            print("Você digitou 0!")
            break

        else:

            if (numero >= 100) and (numero <= 200):

                cont += 1


    menu = f"""

    Foram digitados: {cont} vezes valores entre 100-200!

    Foram contabilizados {valores} valores

    """

    print(menu)


#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano e uma mortalidade de 5% no pais A e 8% no pais B, fazer um programa que
#calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.

#implemento de

def ex12():

    pais_a = 5000000 # 3%   #5
    pais_b = 7000000 # 2%   #8
    ano = 0

    while (pais_a < pais_b):

        # Aumento populacional devido à taxa de natalidade
        pais_a += pais_a * 0.03
        pais_b += pais_b * 0.02

        # Aplicação da mortalidade
        pais_a -= pais_a * 0.05
        pais_b -= pais_b * 0.08

        ano += 1


    menu = f"""

    País A: {pais_a:.2f} habitantes
    País B: {pais_b:.2f} habitantes

    {ano} anos se passaram!

    """

    print(menu)


#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• Amédia de consumo dos tipos 1 e 2

def ex13():

    for _ in range(10,-1,-1):

        num = random.randrange(500)
        tipo = random.randrange(1,2,3)
        total = 0
        kwh = random.randrange(500)
        meses = 0

        if (tipo == 1):

            kwh += kwh*0.3
            total += kwh
            meses += 1

        elif (tipo == 2):

            kwh += kwh*0.5
            total += num
            meses += 1

        elif (tipo == 3):

            kwh += kwh*0.7
            total += num
            meses += 1

    menu = f"""

    Consumo geral: {total} Kwh
    Numero de meses: {meses}

    """

    print(menu)

#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n

def ex14():

    num = int(input("Digite um numero: "))
    # print (math.factorial(num))

    soma = 1

    for num in range (num, 0, -1):

        soma *= num
        print(f"Valor de num: {num}")
        print(f"Valor da Soma: {soma}\n")

#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos

def ex15():

    menor = 0
    maior = 0

    for _ in range (5):
                
        idade = int(input("Digite sua idade: "))

        if (idade<21):

            menor += 1

        elif (idade>50):

            maior += 1

    resultado = f"""

    Pessoas com menos de 21 anos: {menor}
    Pessoas com mais de 50 anos: {maior}
    
    """

    print(resultado)


#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão
    
def ex16():

    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    cont = 0

    if (divisor <= 0):

       dividendo -= divisor
       cont += 1

       print(f" Dividendo: {dividendo}") 
       print(f" Soma: {cont}") 

    conta = f"""

{dividendo}/{divisor}

Dividendo: {dividendo}
Divisor: {divisor}
Quociente: {quociente}
Resto da Divisão: {resto}

"""

    print(conta)

ex16()

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#72 Aula 3. Estruturas de Iteração
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

#19. Emuma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado comnota >= 7.0

#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.

#21. Emuma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número demultas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir tambémo número da carteira domotorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar umvalor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito umabatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.
