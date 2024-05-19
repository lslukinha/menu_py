favoritos = []

def add_receita():
    file = open("menu.txt", "a")
    nome = input("Digite o nome da receita: ")
    pais_origem = input("Digite o país de origem da receita: ")
    ingredientes = input("Digite os ingredientes da receita separados por ';': ")
    preparo = input("Digite o modo de preparo da receita separado por ';': ")
    novaReceita = f"Nome da Receita: {nome}\nPaís de origem: {pais_origem}\nIngredientes da Receita: {ingredientes}\nPreparo: {preparo}\n\n"
    file.write(novaReceita)
    file.close()
    print("Nova receita adicionada com sucesso!")

def att_receita():
    nome_antigo = input("Digite o nome da receita que deseja atualizar: ")
    encontrou = False

    file = open("menu.txt", "r")
    linhas = file.readlines()
    file.close()

    file = open("menu.txt", "w")
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

    file.close()

    if encontrou:
        print("Receita atualizada com sucesso!")
    else:
        print("Receita não encontrada.")

def visualizar_receitas():
    file = open("menu.txt", "r")
    print(file.read())
    file.close()

def add_favorito():
    nome_receita = input("Digite o nome da receita que deseja marcar como favorita: ")
    file = open("menu.txt", "r")
    linhas = file.readlines()
    file.close()

    encontrou = False
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
def filtrar_paises():
    pais_filtro = input("Digite o país de origem para filtrar as receitas: ").strip().lower()
    encontrou_resultado = False
    file = None
    
    file = open("menu.txt", "r")
    receitas = file.readlines()
    for receita in receitas:
        if f"país de origem: {pais_filtro}" in receita.lower():
            print(receita)
            encontrou_resultado = True
    file.close()
    
    if not encontrou_resultado:
        print(f"Não foram encontradas receitas do país '{pais_filtro.capitalize()}'.")
        
def remover_receita():
    nome_receita = input("Digite o nome da receita que deseja remover: ")
    encontrou = False

    file = open("menu.txt", "r")
    linhas = file.readlines()
    file.close()

    file = open("menu.txt", "w")
    i = 0
    while i < len(linhas):
        if nome_receita in linhas[i]:
            encontrou = True
            print("Receita removida:", linhas[i].strip())
            i += 5
        else:
            file.write(linhas[i])
            i += 1

    file.close()

def menu_principal():
    while True:
        print('''
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝\n\n''')
        print('''𝟏- 𝐀𝐝𝐢𝐜𝐢𝐨𝐧𝐚𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚''')
        print('''𝟐- 𝐀𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚''')
        print('''𝟑- 𝐂𝐨𝐥𝐨𝐜𝐚𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚 𝐜𝐨𝐦𝐨 𝐟𝐚𝐯𝐨𝐫𝐢𝐭𝐚''')
        print('''𝟒- 𝐕𝐢𝐬𝐮𝐚𝐥𝐢𝐳𝐚𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚𝐬''')
        print('''𝟓- 𝐕𝐢𝐬𝐮𝐚𝐥𝐢𝐳𝐚𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚𝐬 𝐟𝐚𝐯𝐨𝐫𝐢𝐭𝐚𝐬''')
        print('''𝟔- 𝐅𝐢𝐥𝐭𝐫𝐚𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚𝐬 𝐩𝐨𝐫 𝐩𝐚𝐢́𝐬''')
        print('''𝟕- 𝐑𝐞𝐦𝐨𝐯𝐞𝐫 𝐫𝐞𝐜𝐞𝐢𝐭𝐚''')
        print('''𝟖- 𝐒𝐚𝐢𝐫''')
        escolha = input('''𝐄𝐬𝐜𝐨𝐥𝐡𝐚 𝐚 𝐨𝐩𝐜̧𝐚̃𝐨 𝐝𝐞𝐬𝐞𝐣𝐚𝐝𝐚 (𝟏-𝟖): ''')

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
            break
        else:
            print("Opção inválida. Tente novamente.")

def visualizar_favoritos():
    if favoritos:
        print("Receitas Favoritas:")
        for receita in favoritos:
            print(receita)
    else:
        print("Nenhuma receita favorita marcada.")

while True:
    menu_principal()
