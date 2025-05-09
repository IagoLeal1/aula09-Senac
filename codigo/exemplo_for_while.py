# Explicando for while

# Exemplo de for

lstValores = []

for i in range(5):
    num = int(input("Digite um número: "))
    lstValores.append(num)
    lstValores.sort()

print(f"Os números digitados foram: {lstValores}")

# Exemplo de while

lstNomes = []
resposta = ''

while resposta != 'n':
    nome = input("Digite um nome: ")
    lstNomes.append(nome)

    resposta = input("Deseja continuar? (s/n): ")[0].lower()

print(f"Os nomes digitados foram: {lstNomes}")

lstNomes2 = []

while True:
    nome = input("Digite um nome: ")
    lstNomes2.append(nome)

    resposta = input("Deseja continuar? (s/n): ")[0].lower()

    if resposta == 'n':
        break

    print(f"Os nomes digitados foram: {lstNomes2}")