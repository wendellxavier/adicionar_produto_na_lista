vendas = []

while True:
    produto = input('Qual produto você quer adicionar na lista ? ')
    if not produto:
        break
    quantidade = input('Qual a quantidade? ')
    if not quantidade.isnumeric():
        print('Digite apenas número !!!')
    else:
        quantidade = (int(quantidade))

        vendas.append([produto, quantidade])
        print(f'Voê adicionou na lista: {quantidade} {produto}')