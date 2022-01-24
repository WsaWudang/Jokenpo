#JOGO JOKENPO 
from random import randint 
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

#Inicio
print("""Qual a sua escolha:
[0] = PEDRA
[1] = PAPEL
[2] = TESOURA""")
usuario = int(input("Qual a sua jogada ? "))

#suspense
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("-=" * 11)

#mostrar resultados
print(f"Computador jogou: {itens[computador]}")
print(f"Você jogou: {itens[usuario]}")
print("-=" * 11)

#computador escolhendo pedra
if computador == 0:
    if usuario == 0:
        print("DEU EMPATE")
    elif usuario == 1:
        print("VOCÊ GANHOU")
    elif usuario == 2:
        print("COMPUTADOR GANHOU")
    else:
        print("JOGADA INVÁLIDA")

#computador esolhendo papel
if computador == 1:
    if usuario == 0:
        print("VOCÊ GANHOU")
    elif usuario == 1:
        print("DEU EMPATE")
    elif usuario == 2:
        print("COMPUTADOR GANHOU")
    else:
        print("JOGADA INVÁLIDA")

#computador escolhendo tesoura
if computador == 2:
    if usuario == 0:
        print("VOCÊ GANHOU")
    elif usuario == 1:
        print("COMPUTADOR GANHOU")
    elif usuario == 2:
        print("DEU EMPATE")
    else:
        print("JOGADA INVÁLIDA")