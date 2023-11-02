from random import choice

#placar do Jogo
jogadorVitorias = 0
cpuVitorias = 0
empate = 0


#Função do jogador
def opcaoJogador():
    esc_jogador  = input("Escolha Pedra, Papel ou Tesoura: ").lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção inválida, Tente novamente")
        opcaoJogador()


#Função da máquina IA
def opcaoCpu():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


#Laço de Repetição
while True:

    print("=-" * 15)
    esc_jogador = opcaoJogador()
    esc_maquina = opcaoCpu()
    print("=-" * 15)

#Desenvolvimento do jogo

    #Jogador ganha
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
            or (esc_jogador == "papel") and (esc_maquina == "pedra") \
                or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
                    print(f"Parabéns você escolheu {esc_jogador} e a máquina escolheu {esc_maquina}, Você venceu!")
                    jogadorVitorias += 1

    # Jogador empata
    elif (esc_jogador == esc_maquina):
        print("A rodada ficou empatada!")
        empate += 1

    #Jogador Perde
    else:
        print(f"A máquina venceu, você escolheu {esc_jogador} e a máquina escolheu {esc_maquina}.")
        cpuVitorias += 1

#placar do jogo
    print("=-" * 15)
    print(f"Vitórias do Jogador: {jogadorVitorias}")
    print(f"Empates: {empate}")
    print(f"Vitórias da Máquina {cpuVitorias}")
    print("=-" * 15)

#Jogar novamente
    esc_jogador = input("Você deseja jogar novamente? ").lower()
    if esc_jogador in ["s", "si", "sim"]:
        pass
    elif esc_jogador in ["n", "na", "nã", "não"]:
        break
    else:
        break