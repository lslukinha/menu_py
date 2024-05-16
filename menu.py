def add_receita(receitas_array):
    nome = input("Digite o nome da receita : ")
    pais_origem = input("Digite o país de origem da receita : ")
    ingredientes = input("Digite os ingredientes da receita separados por ';' : ")
    preparo = input("Digite o modo de preparo da receita separado por ';' : ")
    novaReceita = {"nome": nome,"pais_origem": pais_origem,"ingredientes": ingredientes.split(';'),"preparo": preparo.split(';')}
    receitas_array.append(novaReceita)
    print("Nova receita adicionada com sucesso!")
receitas_array=[]
while True:
    print("\nMenu:")
    print("1- Adicionar receita")
    print("2- Atualizar")
    print("3- Filtrar país")
    print("4- Visualizar receitas")
    print("5- Excluir")
    escolha = input("Escolha a opção desejada(1-5): ")

    if escolha == "1":
        add_receita(receitas_array)