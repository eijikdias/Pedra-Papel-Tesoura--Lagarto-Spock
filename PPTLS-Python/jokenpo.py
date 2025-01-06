import random
from time import sleep

#Contador de vitórias de cada jogador:
jogador_vitorias = 0
computador_vitorias = 0

#Variáveis para facilitar:
pedra = 1
papel = 2
tesoura = 3
lagarto = 4
spock = 5

#Pedra Papel Tesoura Lagarto Spock:
print('-=' * 30)
print('            Pedra Papel Tesoura Lagarto Spock')
print('-=' * 30)

#Explicação:
print('''Primeiro vamos às regras:
- Tesoura corta Papel
- Papel cobre Pedra
- Pedra esmaga Lagarto
- Lagarto envenena Spock
- Spock quebra Tesoura
- Tesoura decapita Lagarto
- Lagarto come Papel
- Papel refuta Spock
- Spock vaporiza Pedra
- Pedra amassa Tesoura''')
print('-=' * 30)

#Escolha do computador:
opcoes = [pedra, papel, tesoura, lagarto, spock]
computador = random.choice(opcoes)

#Opções do jogador:
jogada = int(input('''Qual Sua jogada:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
[ 4 ] Lagarto
[ 5 ] Spock\n'''))
print('-=' * 30)

print('PEDRA')
sleep(0.4)
print('PAPEL')
sleep(0.4)
print('TESOURA')
sleep(0.4)
print('LAGARTO')
sleep(0.4)
print('SPOCK!')
print('-' *60)

print('Jogador escolheu {}. Computador escolheu {}'.format(jogada, computador))

#Jogador vencedor:
if jogada == tesoura and computador == papel:
    print('Computador cortado! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == papel and computador == pedra:
    print('Computador coberto! JOGADOR VENCE')
    jogador_vitorias += 1
elif jogada == pedra and computador == lagarto:
    print('Computador esmagado! JOGADOR VENCE')
    jogador_vitorias += 1
elif jogada == lagarto and computador == spock:
    print('Computador envenenado! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == spock and computador == tesoura:
    print('Computador quebrado! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == tesoura and computador == lagarto:
    print('Computador decapitado! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == lagarto and computador == papel:
    print('Computador comido! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == papel and computador == spock:
    print('Computador refutado! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == spock and computador == pedra:
    print('Computador vaporizado! JOGADOR VENCE!')
    jogador_vitorias += 1
elif jogada == pedra and computador == tesoura:
    print('Computador amassado! JOGADOR VENCE!')
    jogador_vitorias += 1

print('-=' * 30)

#Computador vencedor:
if computador == tesoura and jogada == papel:
    print('Jogador cortado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == papel and jogada == pedra:
    print('Jogador coberto! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == pedra and jogada == lagarto:
    print('Jogador esmagado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == lagarto and jogada == spock:
    print('Jogador envenenado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == spock and jogada == tesoura:
    print('Jogador quebrado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == tesoura and jogada == lagarto:
    print('Jogador decapitado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == lagarto and jogada == papel:
    print('Jogador comido! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == papel and jogada == spock:
    print('Jogador refutado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == spock and jogada == pedra:
    print('Jogador vaporizado! COMPUTADOR VENCE!')
    computador_vitorias += 1
elif computador == pedra and jogada == tesoura:
    print('Jogador amassado! COMPUTADOR VENCE!')
    computador_vitorias += 1

if jogada == computador:
    print('UAU! EMPATE!')
    jogador_vitorias += 1
    computador_vitorias += 1
    print('-=' * 30)

#Quer jogar novamente?
escolha = int(input('''Quer jogar novamente?
[ 1 ] Sim
[ 2 ] NÃO\n'''))

while escolha != 2:
    #Pedra Papel Tesoura Lagarto Spock:
    print('-=' * 30)
    print('            Pedra Papel Tesoura Lagarto Spock')
    print('-=' * 30)

     #Escolha do computador:
    opcoes = [pedra, papel, tesoura, lagarto, spock]
    computador = random.choice(opcoes)

    #Opções do jogador:
    jogada = int(input('''Qual Sua jogada:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
[ 4 ] Lagarto
[ 5 ] Spock\n'''))
    print('-=' * 30)

    print('PEDRA')
    sleep(0.4)
    print('PAPEL')
    sleep(0.4)
    print('TESOURA')
    sleep(0.4)
    print('LAGARTO')
    sleep(0.4)
    print('SPOCK!')
    print('-' *60)

    print('Jogador escolheu {}. Computador escolheu {}'.format(jogada, computador))

    #Jogador vencedor:
    if jogada == tesoura and computador == papel:
        print('Computador cortado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == papel and computador == pedra:
        print('Computador coberto! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == pedra and computador == lagarto:
        print('Computador esmagado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == lagarto and computador == spock:
        print('Computador envenenado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == spock and computador == tesoura:
        print('Computador quebrado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == tesoura and computador == lagarto:
        print('Computador decapitado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == lagarto and computador == papel:
        print('Computador comido! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == papel and computador == spock:
        print('Computador refutado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == spock and computador == pedra:
        print('Computador vaporizado! JOGADOR VENCE!')
        jogador_vitorias += 1
    elif jogada == pedra and computador == tesoura:
        print('Computador amassado! JOGADOR VENCE!')
        jogador_vitorias += 1

    print('-=' * 30)

    #Computador vencedor:
    if computador == tesoura and jogada == papel:
        print('Jogador cortado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == papel and jogada == pedra:
        print('Jogador coberto! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == pedra and jogada == lagarto:
        print('Jogador esmagado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == lagarto and jogada == spock:
        print('Jogador envenenado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == spock and jogada == tesoura:
        print('Jogador quebrado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == tesoura and jogada == lagarto:
        print('Jogador decapitado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == lagarto and jogada == papel:
        print('Jogador comido! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == papel and jogada == spock:
        print('Jogador refutado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == spock and jogada == pedra:
        print('Jogador vaporizado! COMPUTADOR VENCE!')
        computador_vitorias += 1
    elif computador == pedra and jogada == tesoura:
        print('Jogador amassado! COMPUTADOR VENCE!')
        computador_vitorias += 1

    if jogada == computador:
        print('UAU! EMPATE!')
        jogador_vitorias += 1
        computador_vitorias += 1
        print('-=' * 30)

    #Quer jogar novamente?
    escolha = int(input('''Quer jogar novamente?
[ 1 ] Sim
[ 2 ] NÃO\n'''))

if escolha == 2:
    print('-=' *30)
    print('                       P L A C A R')
    print('-=' * 30)
    print('''JOGADOR: {}
COMPUTADOR: {}'''.format(jogador_vitorias, computador_vitorias))
    print('O vencedor é...')
    sleep(0.5)
    if jogador_vitorias < computador_vitorias:
        print('\033[34mO COMPUTADOR!\033[0m') 
    elif computador_vitorias < jogador_vitorias:
        print('\033[34mO JOGADOR!\033[0m')
    elif jogador_vitorias == computador_vitorias:
        print('\033[34mEMPATE!\033[0m')

print('-=' * 30)



#Fim do jogo
print("Fim do jogo")