def cadastrar(num):
    for i in range(num):
        nome = input("Informe seu nome: ")
        valor = input("Informe valor da venda: ")

        loja = {
            "Nome": nome,
            "Valor": valor,
        }

        listaCadastro.append(loja)


listaCadastro = []

qtd = int(input("Quantas Pessoas deseja cadastrar? "))
cadastrar(qtd)

print(listaCadastro)