import os

favoritos = []
receitas = []

def terminal_clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    with open("menu.txt", "r") as file:
        print("Receitas no menu:")
        for line in file:
            print(line.strip())

def add_receita():
    terminal_clean()
    with open("menu.txt", "a") as file:
        while True:
            nome = input("Digite o nome da receita: ").strip()
            if nome:
                break
            terminal_clean()
            print("Digite novamente o nome da receita")

        while True:
            pais_origem = input("Digite o país de origem da receita: ").strip()
            if pais_origem:
                break
            terminal_clean()
            print("Digite novamente o país de origem da receita")

        while True:
            ingredientes = input("Digite os ingredientes da receita separados por ';': ").strip()
            if ingredientes:
                break
            terminal_clean()
            print("Digite novamente os ingredientes da receita")

        while True:
            preparo = input("Digite o modo de preparo da receita separado por ';': ").strip()
            if preparo:
                break
            terminal_clean()
            print("Digite novamente o modo de preparo da receita")

        novaReceita = (
            f"Nome da Receita: {nome}\n"
            f"País de origem: {pais_origem}\n"
            f"Ingredientes da Receita: {ingredientes}\n"
            f"Preparo: {preparo}\n\n"
        )
        file.write(novaReceita)
        print("Nova receita adicionada com sucesso!")

def att_receita():
    terminal_clean()
    exibir_menu()

    nome_antigo = input("Digite o nome da receita que deseja atualizar: ")
    encontrou = False

    with open("menu.txt", "r") as file:
        linhas = file.readlines()

    with open("menu.txt", "w") as file:
        i = 0
        while i < len(linhas):
            if nome_antigo in linhas[i]:
                encontrou = True
                nome_novo = input("Digite o novo nome da receita (ou pressione Enter para manter o atual): ").strip() or linhas[i].split(": ")[1].strip()
                pais_origem_novo = input("Digite o novo país de origem da receita (ou pressione Enter para manter o atual): ").strip() or linhas[i+1].split(": ")[1].strip()
                ingredientes_novo = input("Digite os novos ingredientes da receita separados por ';' (ou pressione Enter para manter os atuais): ").strip() or linhas[i+2].split(": ")[1].strip()
                preparo_novo = input("Digite o novo modo de preparo da receita separado por ';' (ou pressione Enter para manter o atual): ").strip() or linhas[i+3].split(": ")[1].strip()
                novaReceita = (
                    f"Nome da Receita: {nome_novo}\n"
                    f"País de origem: {pais_origem_novo}\n"
                    f"Ingredientes da Receita: {ingredientes_novo}\n"
                    f"Preparo: {preparo_novo}\n\n"
                )
                file.write(novaReceita)
                i += 5
            else:
                file.write(linhas[i])
                i += 1

    if encontrou:
        print("Receita atualizada com sucesso!")
    else:
        print("Receita não encontrada.")

def visualizar_receitas():
    terminal_clean()
    with open("menu.txt", "r") as file:
        print(file.read())
    retornar=input("Pressione Enter para voltar ao menu principal...")
    terminal_clean()

def add_favorito():
    terminal_clean()
    exibir_menu()

    nome_receita = input("Digite o nome da receita que deseja marcar como favorita: ")
    encontrou = False

    with open("menu.txt", "r") as file:
        linhas = file.readlines()

    i = 0
    while i < len(linhas):
        if nome_receita in linhas[i]:
            encontrou = True
            favoritos.append("".join(linhas[i:i+5]))
            print("Receita marcada como favorita!")
            break
        i += 1

    if not encontrou:
        print("Receita não encontrada.")

def visualizar_favoritos():
    terminal_clean()
    if favoritos:
        print("Receitas Favoritas:")
        for receita in favoritos:
            print(receita)
    else:
        print("Nenhuma receita favorita marcada.")
    retornar= input("Pressione Enter para voltar ao menu principal...")
    terminal_clean()

def filtrar_paises():
    terminal_clean()
    exibir_menu()

    pais_filtro = input("Digite o país de origem para filtrar as receitas: ").strip().lower()
    encontrou_resultado = False

    with open("menu.txt", "r") as file:
        receitas = file.readlines()
        for i in range(0, len(receitas), 5):
            if f"País de origem: {pais_filtro}" in receitas[i+1].strip().lower():
                print(receitas[i], receitas[i+1], receitas[i+2], receitas[i+3], receitas[i+4], sep="")
                encontrou_resultado = True

    if not encontrou_resultado:
        print(f"Não foram encontradas receitas do país '{pais_filtro.capitalize()}'.")

def remover_receita():
    terminal_clean()
    exibir_menu()

    nome_receita = input("Digite o nome da receita que deseja remover: ")
    encontrou = False

    with open("menu.txt", "r") as file:
        linhas = file.readlines()

    with open("menu.txt", "w") as file:
        i = 0
        while i < len(linhas):
            if nome_receita in linhas[i]:
                encontrou = True
                print("Receita removida:", linhas[i].strip())
                i += 5
            else:
                file.write(linhas[i])
                i += 1

    if not encontrou:
        print("Receita não encontrada.")

def sugerir_receita():
    terminal_clean()
    with open("menu.txt", "r") as file:
        linhas = file.readlines()

    receitas.clear()
    i = 0
    while i < len(linhas):
        if "Nome da Receita:" in linhas[i]:
            receita = "".join(linhas[i:i+5])
            receitas.append(receita)
            i += 5
        else:
            i += 1

    if receitas:
        numero_sugestao = int(input("Digite um número para sugerir uma receita: "))
        numero_aleatorio = numero_sugestao % len(receitas)
        sugestao = receitas[numero_aleatorio]
        print("Sugestão de receita:")
        print(sugestao)
    else:
        print("Não há receitas disponíveis para sugerir.")
        
def adicionar_nota_pessoal():
    terminal_clean()
    exibir_menu()
    nome_receita = input("Digite o nome da receita à qual deseja adicionar uma nota pessoal: ")
    encontrou = False

    with open("menu.txt", "r") as file:
        linhas = file.readlines()

    i = 0
    while i < len(linhas):
        if nome_receita in linhas[i]:
            encontrou = True
            nota_pessoal = input("Digite sua nota pessoal para esta receita: ")
            linhas.insert(i + 4, f"Nota Pessoal: {nota_pessoal}\n")
            print("Nota pessoal adicionada com sucesso.")
            break
        i += 5

    if encontrou:
        with open("menu.txt", "w") as file:
            file.writelines(linhas)
    else:
        print("Receita não encontrada.")

while True:
    terminal_clean()
    print('''
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██████╗░██████╗░██╗███╗░░██╗██████╗░██╗██████╗░███████╗██╗░░░░░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔════╝██║░░░░░
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝\n\n''')
    print('''1- Adicionar Receita''')
    print('''2- Atualizar receita''')
    print('''3- Colocar receita como favorita''')
    print('''4- Visualizar receitas''')
    print('''5- Visualizar receitas favoritas''')
    print('''6- Filtrar receitas por país''')
    print('''7- Remover receita''')
    print('''8- Sugerir receita''')
    print('''9- Dar Nota''')
    print('''10- Sair''')
    escolha = input('''Escolha a opção desejada (1-10): ''')

    if escolha == "1":
        add_receita()
    elif escolha == "2":
        att_receita()
    elif escolha == "3":
        add_favorito()
    elif escolha == "4":
        visualizar_receitas()
    elif escolha == "5":
        visualizar_favoritos()
    elif escolha == "6":
        filtrar_paises()
    elif escolha == "7":
        remover_receita()
    elif escolha == "8":
        sugerir_receita()
    elif escolha == "9":
        adicionar_nota_pessoal()
    elif escolha == "10":
        break
    else:
        print("Opção inválida. Tente novamente.")
