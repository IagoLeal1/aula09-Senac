# Cadastrar um novo vendedor e o valor da venda
def cadastrar(num):
    for i in range(num):
        nome = input("Informe o nome do vendedor: ")
        valor = float(input("Informe valor da venda: "))

        loja = {
            "Nome": nome,
            "Valor": valor,
        }

        listaCadastro.append(loja)


# Calcular o Total e a Media de Vendas
def calculaTotalMedia():
    tot = 0
    for pessoa in listaCadastro:
        tot += float(pessoa["Valor"])

    med = tot / len(listaCadastro)

    return tot, med    


# Buscar o maior valor e o vendedor
def buscaMaior():
    maior = 0
    vendedor = ''

    for v in listaCadastro:
        if v["Valor"] > maior:
            maior = v["Valor"]
            vendedor = v["Nome"]

    return maior, vendedor


# Buscar um vendedor específico
def buscaVendedor(nome):
    for v in listaCadastro:
        if v["Nome"] == nome:
            return v


# Exemplo 01 cadastrar funcionário
listaCadastro = []

qtd = int(input("Quantas Pessoas deseja cadastrar? "))
cadastrar(qtd)

print(30*"=")
print(listaCadastro)

# Exemplo 02 calcular total e média
total, media = calculaTotalMedia()

print(30*"=")
print(f"O total de vendas é: {total}")
print(f"A média de vendas é: {media}")

# Exemplo 03 - Maior Valor e Vendedor

maiorVenda, maiorVendedor = buscaMaior()

print(30*"=")
print(f"A maior venda foi de {maiorVenda}")
print(f"O vendedor que fez a maior venda foi {maiorVendedor}")

# Exemplo 04 - Buscar Vendedor

print(30*"=")
respostaVendedor = input("Gostaria de buscar um vendedor? (s/n):  ")[0].lower()

if respostaVendedor == 's':
    vendeorSelecionado = input("Informe o nome do vendedor: ")
    vendedor = buscaVendedor(vendeorSelecionado)

    if vendedor:
        print(f"Vendedor: {vendedor['Nome']}")
        print(f"Valor da Venda: {vendedor['Valor']}")
    else:
        print("Vendedor não encontrado")
else:
    print("Ok, programa encerrado")