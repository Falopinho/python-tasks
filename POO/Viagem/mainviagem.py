from classviagem import viagem

destino01 = viagem("Flórida")
destino02 = viagem("Monaco")
destino03 = viagem("Manchester")
destino04 = viagem("Veneza")
destino05 = viagem("Rio de Janeiro")
destino06 = viagem("Vancouver")

print("Olá, Temos algumas opções de viagens em diferentes lugares do mundo pra você!")
viajante = input("Antes de começarmos, qual é o seu nome? ")
print(f"Certo {viajante}, temos 6 opções de viagens para você..."
'''    
[0] Flórida
[1] Monaco
[2] Manchester
[3] Veneza
[4] Rio de Janeiro
[5] Vancouver
''')

selecao = int(input("Selecione o número da viagem desejada: "))
list_viagem = [destino01, destino02, destino03, destino04, destino05, destino06]

for opção in list_viagem:
    if selecao <= 5:
        print(f"{viajante} sua viagem para {list_viagem[selecao].destino} está marcada.")
        print("Volte sempre!")
        break
    else:
        print("Esta opção não está incluída em nossos destinos.")
        selecao = int(input("Selecione o número da viagem desejada: "))
        break