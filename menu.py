def add_receita():
    file = open("menu.txt","a")
    nome = input("Digite o nome da receita : ")
    pais_origem = input("Digite o país de origem da receita : ")
    ingredientes = input("Digite os ingredientes da receita separados por ';' : ")
    preparo = input("Digite o modo de preparo da receita separado por ';' : ")
    novaReceita =  f"Nome da Receita: {nome}\nPaís de origem: {pais_origem}\nIngredientes da Receita: {ingredientes}\nPreparo: {preparo}\n\n"
    print(novaReceita)
    file.write(novaReceita)
    file.close()
    print("Nova receita adicionada com sucesso!")

def att_receita():
    file = open("menu.txt","r")
    file.write(novaReceita)
    nome_antigo = input("Digite o nome da receita que deseja atualizar: ")
    encontrou = False

    with open("menu.txt", "r") as file:
        linhas = file.readlines()

    with open("menu.txt", "w") as file:
        i = 0
        while i < len(linhas):
            if nome_antigo in linhas[i]:
                encontrou = True
                nome_novo = input("Digite o novo nome da receita (ou pressione Enter para manter o atual): ") or linhas[i].split(": ")[1].strip()
                pais_origem_novo = input("Digite o novo país de origem da receita (ou pressione Enter para manter o atual): ") or linhas[i+1].split(": ")[1].strip()
                ingredientes_novo = input("Digite os novos ingredientes da receita separados por ';' (ou pressione Enter para manter os atuais): ") or linhas[i+2].split(": ")[1].strip()
                preparo_novo = input("Digite o novo modo de preparo da receita separado por ';' (ou pressione Enter para manter o atual): ") or linhas[i+3].split(": ")[1].strip()
                novaReceita = f"Nome da Receita: {nome_novo}\nPaís de origem: {pais_origem_novo}\nIngredientes da Receita: {ingredientes_novo}\nPreparo: {preparo_novo}\n\n"
                file.write(novaReceita)
                i += 5  
            else:
                file.write(linhas[i])
                i += 1
                print('teste2')

    if encontrou:
        print("Receita atualizada com sucesso!")
    else:
        print("Receita não encontrada.")

def visualizarReceitas(novaReceita):
    file = open("menu.txt","r")
    file.write(novaReceita)
    file.close()

while True:
    print("\nMenu:")
    print("1- Adicionar receita")
    print("2- Atualizar")
    print("3- Filtrar país")
    print("4- Visualizar receitas")
    print("5- Excluir")
    escolha = input("Escolha a opção desejada(1-5): ")

    if escolha == "1":
         add_receita()
    elif escolha =="4":
        visualizarReceitas()