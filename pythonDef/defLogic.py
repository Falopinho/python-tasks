'''
Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.

a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles
'''

#Obtendo valores e declarando váriaveis
x = float(input("Escolha um número: "))
y = float(input("Escolha outro número: "))


#criando função para somar valores
def maiorNum():
    global x, y
    if (x > y):
        return x
    elif (y > x):
        return y
    else:
        print("Opção inválida.")
        maiorNum()


def mediaNum():
    global x, y
    return ((x + y) / 2)


#Transformando funções em váriaveis
fun = maiorNum()
media = mediaNum()

#Obtendo resposta e chamando a função
print(f"O maior número entre, {x} e {y} é {fun}")
print(f"E a média aritmética de {x} e {y} é igual a {media}")
