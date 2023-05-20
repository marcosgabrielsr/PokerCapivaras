# *************************************************************************
# * Aluno: Marcos Gabriel da Silva Rocha
# * Trabalho 1 - Poker das Capivara
# * Professor: Marco Aurélio
# *************************************************************************

# Dados:
# J, Q, K e A valem respectivamente 11, 12, 13 e 14
# Tipos de mãos:
#   • Flush: 5 cartas de quaisquer valores com o mesmo naipe
#   • Sequência: 5 cartas com valores em sequência (p. ex. 4, 5, 6, 7 e 8)
#   • Quadra: 4 cartas com o mesmo valor
#   • Trinca: 3 cartas com o mesmo valor
#   • 2 pares: 2 cartas com o mesmo valor em conjunto com outras 2 cartas de um mesmo valor
#   • Par: 2 cartas com o mesmo valor
#   • Carta mais alta: se nenhuma das mãos acima ocorre, é considerada a carta de maior valor
# Entrada:
#   • Valores/Nipes -> valores de 2 a 10 e J, Q, K e A / naipes: P, C, E e O

#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Função que troca os caracteres das cartas por números
def charForNum(x):
    if x == 'J':
        x = 11
    elif x == 'Q':
        x = 12
    elif x == 'K':
        x = 13
    elif x == 'A':
        x = 14
    else:
        x = int(x)

    return x

#Função que compara verifica se o primeiro naipe do argumento retornando True or False
def likenSuits(a, b):
    listaNaipes = ['O', 'E', 'C', 'P']
    if listaNaipes.index(a) > listaNaipes.index(b):
        return True
    else:
        return False

#Função que verfica se a mão do jogador é do tipo flush
def isFlush(t):
    if t.count('P') == 5 or t.count('C') == 5 or t.count('E') == 5 or t.count('O') == 5:
        return True

    return False

#Função que verifica se a mão do jogador é do tipo sequencia
def isSequencia(s):
    s = sorted(s)
    count = 0

    for i in range(len(s)):
        if i != len(s) - 1 and (s[i + 1] - s[i]) == 1:
            count += 1

    if count == 4:
        return True
    else:
        return False

#Função que verifica se a mão do jogador é do tipo quadra
def isQuadra(s):
    for i in range(2, 15):
        if s.count(i) == 4:
            return True

    return False

#Função que verifica se a mão do jogador é do tipo trinca
def isTrinca(s):
    for i in range(2, 15):
        if s.count(i) == 3:
            return True

    return False

#Função que verifica se a mão do jogador é do tipo pares
def is2Pares(s):
    contador = 0
    for i in range(2, 15):
        if s.count(i) == 2:
            contador += 1
    
    if contador == 2:
        return True
    else:
        return False

#Função que verifica se a mão do jogar é do tipo par
def isPar(s):
    for i in range(2, 15):
        if s.count(i) == 2:
            return True

    return False

#Função que analisa as cartas do jogador e retorna qual a maior
def topCard(s, t):
    carta = max(s)
    naipe = t[s.index(max(s))]
    
    return carta, naipe

#Função que utiliza das demais acima para gerenciar e retornar por meio de strings e dados numéricos o tipo de mão do jogador e o poder da mão do mesmo
#respectivamente
def typeHand(s, t):
    if isFlush(t):
        handPower = 6
    elif isSequencia(s):
        handPower = 5
    elif isQuadra(s):
        handPower = 4
    elif isTrinca(s):
        handPower = 3
    elif is2Pares(s):
        handPower = 2
    elif isPar(s):
        handPower = 1
    else:
        handPower = 0

    return handPower

#Recebendo o número de jogadas
n = int(input("Insira o número de jogadas: "))

#Repete as jogadas de acordo com a entrada do usuário
for i in range(n):
    #Criando as listas referentes aos valores e aos nipes das cartas do jogador
    p1V, p2V = [], []
    p1N, p2N = [], []

    #Pegando a mão do jogador 1 e separando os naipes e os valores das cartas
    mao1 = input().split()
    p1V = [charForNum(mao1[a]) for a in range(len(mao1)) if a % 2 != 1]
    p1N = [mao1[a] for a in range(len(mao1)) if a % 2 != 0]

    #Pegando a mão do jogador 2 e separando os naipes e os valores das cartas
    mao2 = input().split()
    p2V = [charForNum(mao2[a]) for a in range(len(mao2)) if a % 2 != 1]
    p2N = [mao2[a] for a in range(len(mao2)) if a % 2 != 0]

    #Recebendo o tipo de mão do jogador 1
    #Recebendo o tipo de mão do jogador 
    pHand1 = typeHand(p1V, p1N)
    pHand2 = typeHand(p2V, p2N)

    #Verifica se a mão de ambos os jogadores é do tipo vazio, significa que não tem nenhuma das combinções listadas anteriormente,
    #logo teremos que pegar a maior carta do jogador
    if pHand1 == 0 and pHand2 == 0:
        #Pegando a maior carta e o seu respectivo naipe
        vl1, np1 = topCard(p1V, p1N)
        vl2, np2 = topCard(p2V, p2N)

        #Se os valores das cartas são iguais, verifica qual tem o maior naipe
        if vl1 == vl2:
            #Se o naipe do player 1 for mais forte que o do player 2
            if likenSuits(np1, np2):
                print(1)
            #Se o naipe do player 2 for maior que o do player 1
            else:
                print(2)
        #Se os valores das cartas forem diferentes, verificam quais são os maiores
        else:
            if vl1 > vl2:
                print(1)
            elif vl1 < vl2:
                print(2)
    #Se pelo menos uma das mãos forem diferentes de 'void', comparamos o poder da mão dos jogadores
    else:  
        if pHand1 > pHand2:
            print(1)
        elif pHand1 < pHand2:
            print(2)
        else:
            print('E')

exit(0)