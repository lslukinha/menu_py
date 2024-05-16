def add_receita():
    file = open("menu.txt","a")
    nome = input("Digite o nome da receita : ")
    pais_origem = input("Digite o país de origem da receita : ")
    ingredientes = input("Digite os ingredientes da receita separados por ';' : ")
    preparo = input("Digite o modo de preparo da receita separado por ';' : ")
    novaReceita =  f"{nome},{pais_origem},{ingredientes},{preparo}\n\n"
    print(novaReceita)
    file.write(novaReceita)
    file.close()
    print("Nova receita adicionada com sucesso!")
def visualizarReceitas(receitas_array):
    for receita in receitas_array:
        print(f"Nome: {receita['nome']}")
        print(f"Pais de origem: {receita['pais_origem']}")
        print("Ingredientes:", receita['ingredientes'])
        print("Preparo:", receita['preparo'])
        print()
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
    elif escolha =="4":
        visualizarReceitas(receitas_array)