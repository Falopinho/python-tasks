'''
Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros).
'''

def potencia():
    base = int(input("Escolha a base: "))
    expoente = int(input("Escolha o expoente: "))
    potencia  = (base ** expoente)
    print(f"A base '{base}' com o expoente '{expoente}' tem a potência de '{potencia}'")

potencia()
    