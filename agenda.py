import os

limpar = lambda: os.system("clear")

agenda = []


def init():
    while True:
        limpar()

        opcoes = {
            "1": "Cadastrar contato",
            "2": "Listar contatos",
            "3": "Editar contato",
            "4": "Marcar como favorito",
            "5": "Listar contatos favoritos",
            "6": "Excluir contato",
            "7": "Sair",
        }

        print("===========================")
        print("AGENDA                     ")
        print("===========================\n")

        for codigo, nome in opcoes.items():
            print(f"[{codigo}] - {nome}")
        
        try:

            opcao = int(input("\nSelecione uma opçao: "))
        
            if opcao == 1:
                cadastrar_contato()
            elif opcao == 2:
                listar_contatos()
            elif opcao == 3:
                editar_contato()
            elif opcao == 4:
                marcar_favorito()
            elif opcao == 5:
                listar_favoritos()
            elif opcao == 6:
                apagar_contato()
            elif opcao == 7:
                break
            else:
                print("Opção inválida")

        except Exception as e:
            print(f"Uma opção inválida foi digitada: {e}")
            input("\nPressione [ENTER] para continuar")


def cadastrar_contato():
    registro = {
        "Nome": "",
        "Telefone": "",
        "Email": "",
        "Favorito": "n"
    }

    for i, item in enumerate(registro):
        limpar()

        print("===========================")
        print("AGENDA: Cadastrar Contato  ")
        print("===========================\n")

        for campo, valor in registro.items():
            print(f"{campo}: {valor}")
        
        registro[item] = input(f"\n{item}: ")

    agenda.append(registro)


def listar_contatos():
    limpar()
    
    print("===========================")
    print("AGENDA: Listar contatos    ")
    print("===========================\n")

    if len(agenda) == 0:
        input("Nenhum contato para exibir.\nPressione [ENTER] para continuar.")
        return

    _listar()

    input("\nPressione [ENTER] para continuar")


def editar_contato():
    limpar()
    
    print("===========================")
    print("AGENDA: Editar contato     ")
    print("===========================\n")

    _listar()

    indice = (int(input("\nDigite o número do contato para ser editado: ")) - 1)

    registro = agenda[indice]

    for i, item in enumerate(registro):
        limpar()

        print("===========================")
        print("AGENDA: Editar contato     ")
        print("===========================\n")

        for campo, valor in registro.items():
            print(f"{campo}: {valor}")

        print("\n(mantenha vazio para não alterar o valor)")
        
        valor = input(f"\n{item}: ")

        if valor != '':
            registro[item] = valor

    agenda[indice] = registro


def marcar_favorito():
    while True:        
        limpar()
        
        print("===========================")
        print("AGENDA: Marcar favorito    ")
        print("===========================\n")

        _listar()

        indice = (int(input("\nDigite o número do contato para marcar/desmarcar como favorito ou zero para voltar: ")) - 1)
        
        if indice == -1:
            break

        registro = agenda[indice]
        registro['Favorito'] = "s" if registro['Favorito'] != "s" else "n"
        agenda[indice] = registro


def listar_favoritos():
    limpar()
            
    print("===========================")
    print("AGENDA: Lista de Favoritos ")
    print("===========================\n")

    favoritos = list(filter(lambda contato: contato['Favorito'] == "s", agenda))

    if len(favoritos) == 0:
        input("Nenhum favorito para exibir.\nPressione [ENTER] para continuar.")
        return

    _listar(favoritos)

    input("\nPressione [ENTER] para continuar")
    

def apagar_contato():
    while True:
        limpar()
            
        print("===========================")
        print("AGENDA: Excluir contato    ")
        print("===========================\n")

        if len(agenda) == 0:
            input("Nenhum registro para ser excluído.\nPressione [ENTER] para continuar.")
            break

        _listar()

        indice = (int(input("\nDigite o número do contato para excluir ou zero para sair: ")) - 1)

        if indice == -1:
            break

        agenda.pop(indice)


def _listar(lista = agenda):
    for indice, registro in enumerate(lista, start=1):
        nome = registro['Nome']
        telefone = registro['Telefone']
        email = registro['Email']
        favorito = "♥" if registro['Favorito'] == "s" else " "

        print(f"[{indice}]. {favorito} Nome: {nome}, Telefone: {telefone}, Email: {email}")

init()