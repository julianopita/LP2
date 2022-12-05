from menu.menuCliente import clientMenu
from menu.menuProduto import productMenu
from menu.menuPedido import orderMenu

def mainMenu(): 
    cont = True   
    while cont == True:
        choice = input("Selecione a opção desejada:\n\n[1] - Consultar, cadastrar, alterar ou deletar clientes.\n[2] - Consultar, cadastrar ou alterar produtos.\n[3] - Consultar ou cadastrar pedidos.\n[0] - Sair do programa\n")

        if choice == '1':
            clientMenu()
        elif choice == '2':
            productMenu()        
        elif choice == '3':
            orderMenu()
        elif choice == '0':
            print("Obrigado por utilizar o gerenciador de lojas!")
            cont = False
        else:
            print("Por favor, escolha uma opção de 1 a 3, ou 0 para sair") 