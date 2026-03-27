import time
import sys
from playsound3 import playsound
import pop
import rap
import rock

print('\nBem vindo ao adivinhe a música, neste pequeno quiz focado exclusivamente no áudio,\nvocê irá escutar pequenos trechos de musicas, e baseado neste pequeno fragmento de \numa música você deve adivinhar qual é a obra apenas baseado no pequeno pedaço escutado. \nVocê poder digitar repetir para ouvir a música novamente, e também, pode digitar dica para saber algumas letras do nome da música. (VOCÊ TEM APENAS 3 VIDAS)')
time.sleep(0)

#POR ENQUANTO, QUALQUER ESTILO RODA O ESTILO 1.
print("\nQual estilo você quer escolher?")
print("1: Rock")
print("2: Pop")
print("3: Rap")

estilo=input("\n").upper()

while estilo != "1" and estilo != "ROCK" and estilo != "2" and estilo != "POP" and estilo != "3" and estilo != "RAP":
    print("Digite um estilo válido!")
    estilo=input("").upper()

if estilo == "1" or estilo == "ROCK":
    print("Você escolheu Rock!")
    print('\nCaso queira iniciar digite sim.')
    comeco = input().upper()
    while comeco != 'SIM':
        print('Caso queira iniciar digite Sim.')
        comeco = input().upper()
    print("Estão vamos começar!")
    rock.rock()

if estilo == "2" or estilo == "POP":
    print("Você escolheu Pop!")
    print('\nCaso queira iniciar digite sim.')
    comeco = input().upper()
    while comeco != 'SIM':
        print('Caso queira iniciar digite Sim.')
        comeco = input().upper()
    print("Estão vamos começar!")
    pop.pop()
        
if estilo == "3" or estilo == "RAP":
    print("Você escolheu Rap!")
    print('\nCaso queira iniciar digite sim.')
    comeco = input().upper()
    while comeco != 'SIM':
        print('Caso queira iniciar digite Sim.')
        comeco = input().upper()
    print("Estão vamos começar!")
    rap.rap()