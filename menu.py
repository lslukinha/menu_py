favoritos = []
receitas = []

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

def visualizar_favoritos():
    if favoritos:
        print("Receitas Favoritas:")
        for receita in favoritos:
            print(receita)
    else:
        print("Nenhuma receita favorita marcada.")

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

def sugerir_receita():
    file = open("menu.txt", "r")
    linhas = file.readlines()
    file.close()
    
    i = 0
    while i < len(linhas):
        if "Nome da Receita:" in linhas[i]:
            nome_receita = linhas[i].split(":")[1].strip()
            receita = linhas[i].strip() + "\n" + linhas[i+1].strip() + "\n" + linhas[i+2].strip() + "\n" + linhas[i+3].strip() + "\n" + linhas[i+4].strip()
            receitas.append(receita)
            i += 4  
        else:
            i += 1
    if receitas:
        numero_sugestão = int(input("Digite um número para sugerir uma receita: "))
        numero_aleatorio= numero_sugestão % len(receitas) 
        sugestao = receitas[numero_aleatorio]
        print("Sugestão de receita:")
        print(sugestao)
    else:
        print("Não há receitas disponíveis para sugerir.")
def buscar_por_ingredientes():
    ingredientes_busca = input("Digite os ingredientes que deseja buscar (separados por vírgula): ").strip().lower().split(',')
    encontrou_resultado = False

    file = open("menu.txt", "r")
    receitas = file.readlines()
    file.close()

    print("Resultados da busca:")
    for i in range(0, len(receitas), 5):
        ingredientes_receita = receitas[i+2].split(": ")[1].strip().lower().split(';')
        if all(ingrediente in ingredientes_receita for ingrediente in ingredientes_busca):
            print(receitas[i], receitas[i+1], receitas[i+2], receitas[i+3], sep="")
            encontrou_resultado = True

    if not encontrou_resultado:
        print("Nenhuma receita encontrada com os ingredientes especificados.")

while True:
        print('''
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝\n\n''')
        print('''1- 🇦​​​​​🇩​​​​​🇮​​​​​🇨​​​​​🇮​​​​​🇴​​​​​🇳​​​​​🇦​​​​​🇷​​​​​ 🇷​​​​​🇪​​​​​🇨​​​​​🇪​​​​​🇮​​​​​🇹​​​​​🇦​​​​​''')
        print('''2- Atualizar receita''')
        print('''3- Colocar receita como favorita''')
        print('''4- Visualizar receitas''')
        print('''5- Visualizar receitas favoritas''')
        print('''6- Filtrar receitas por país''')
        print('''7- Remover receita''')
        print('''8- Sugerir receita''')
        print('''9-Buscar Ingredientes''')
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
            buscar_por_ingredientes()
        
        elif escolha == "10":
            break
        else:
            print("Opção inválida. Tente novamente.")
