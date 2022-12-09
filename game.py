import random

print('*bem vindo no jogo de adivinhação!*')


numeroSecreto = random.randrange(1, 101)
numeroDeTentativas = 0
pontos = 100

print('Qual nível de dificuldade?')
print('-(1) Fácil-  -(2) Médio-  -(3) Difícil- ')

nivelEasy = 7 
nivelMedium = 5
nivelHard = 3

nivel = int(input("define o nível: "))

if(nivel == 1):
    numeroDeTentativas = nivelEasy
elif(nivel == 2):
    numeroDeTentativas = nivelMedium
else:
    numeroDeTentativas = nivelHard

for rodada in range (1, numeroDeTentativas + 1):
    strTentativa = f'tentativa {rodada} de {numeroDeTentativas}'
    print(strTentativa)
    chuteStr = input('Digite um número entre 1 e 100: ')
    print(f'Você digitou: {chuteStr}')
    chute = int(chuteStr)
    
    if (chute <1 or chute > 100):
        print('você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numeroSecreto
    maior   = chute > numeroSecreto
    menor   = chute < numeroSecreto
    
    

    if(acertou):
        print(f'Parabéns, você acertou, seu total de pontos foi {pontos}!')
        break
    else:
        if(maior):
            print('Você errou! Seu chute ultrapassou o número secreto!')
        elif(menor):
            print(' Você errou! Seu chute foi menor que o número secreto')
        pontosPerdidos = abs(numeroSecreto - chute)
        pontos = pontos - pontosPerdidos

print('Fim do Jogo!')
print(f'o numero secreto era: {numeroSecreto}')
