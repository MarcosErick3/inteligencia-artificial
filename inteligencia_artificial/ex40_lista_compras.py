# Exercício 40: Lista de Compras
# Crie um programa para gerenciar uma lista de compras, permitindo adicionar, remover e listar itens.

lista_compras = []

while True:
    print("\n=== LISTA DE COMPRAS ===")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o item a adicionar: ")
        lista_compras.append(item)
        print(f"'{item}' adicionado com sucesso!")
    
    elif opcao == "2":
        if not lista_compras:
            print("A lista está vazia!")
        else:
            print("Itens da lista:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
            indice = int(input("Digite o número do item a remover: ")) - 1
            if 0 <= indice < len(lista_compras):
                item_removido = lista_compras.pop(indice)
                print(f"'{item_removido}' removido com sucesso!")
            else:
                print("Índice inválido!")
    
    elif opcao == "3":
        if not lista_compras:
            print("A lista está vazia!")
        else:
            print("\nItens da sua lista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
    
    elif opcao == "4":
        print("Até logo!")
        break
    
    else:
        print("Opção inválida!")
