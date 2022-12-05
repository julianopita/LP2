from queries.client import Cliente
from utils.validateInput import validarCpf, formatarUpper, validarTel
        
def clientMenu():
    cont = True   
    while cont == True:
        choice = input("Selecione a opção desejada:\n\n[1] - Consultar todos os clientes ou procurar por nome.\n[2] - Cadastrar novo cliente.\n[3] - Alterar dados de um cliente existente.\n[4] - Deletar um cliente existente do sistema.\n[0] - Voltar ao Menu principal.\n")

        #consulta cliente
        if choice == '1':
            #Verificaçao de dados de um cliente:
             nome = input("Insira o nome do cliente a ser consultado, ou enter para ver todos: ")
             clientShow = Cliente(nome = nome)
             resultado = Cliente.show_client_nome("LP2Final.db", clientShow) 
             if resultado == []:
                 print("\nNão existem clientes com este nome (parcial ou total).\n")           
             else:
                 for r in resultado:
                    print("\nCliente: ", r[1],"\n", "cpf:", r[0], "\n", "Endereço:", r[2], "\n", "Telefone:", r[3], "\n", "email:", r[4])

        #insere novo cliente
        elif choice == '2':

            #inserção de cpf 
            cpfVal = False            
            while cpfVal == False:
                cpfVal = validarCpf(input("Insira o cpf do cliente a ser cadastrado com 11 dígitos sem pontuação: "))
            else:
                cpf = cpfVal                
           
            #inserção de nome
            nome = formatarUpper(input("Insira o nome do cliente: "))
                       
            #inserção de endereço
            endereco_res = formatarUpper(input("Insira o endereço residencial do cliente: "))
            
            #inserção de telefone
            telefoneVal = False
            while telefoneVal == False:
                telefoneVal = validarTel(input("Insira o telefone de contato do cliente: "))                
            else:
                telefone = telefoneVal
                
            #inserção de email
            email = input("insira o email do cliente: ")

            #insere os dados validados no BD
            clientNew = Cliente (cpf, nome, endereco_res, telefone, email)
            Cliente.new_client("LP2Final.db", clientNew)
            
            resultado = Cliente.show_client_nome("LP2Final.db", clientNew)             
            for r in resultado:
                print("\nCliente: ", r[1],"\n", "cpf:", r[0], "\n", "Endereço:", r[2], "\n", "Telefone:", r[3], "\n", "email:", r[4])

        #altera cliente existente    
        elif choice == '3':
            #inserção de cpf 
            cpfVal = False            
            while cpfVal == False:
                cpfVal = validarCpf(input("Insira o cpf do cliente a ser alterado com 11 dígitos sem pontuação: "))
            else:
                cpf = cpfVal                         
            
            
            #inserção de nome
            nome = formatarUpper(input("Insira o novo nome do cliente ou Enter para manter o mesmo: "))
                       
            #inserção de endereço
            endereco_res = formatarUpper(input("Insira o novo endereço residencial do cliente ou Enter para manter o mesmo: "))
            
            #inserção de telefone
            telefoneVal = False
            #tele = input("Insira o telefone de contato do cliente: ")
            
            while telefoneVal == False:
                telefoneVal = input("Insira o telefone de contato do cliente: ") 
                match telefoneVal:
                    case "":
                        telefone = ""                      
                    case _:
                        if validarTel(telefoneVal) == False:
                            telefoneVal = False
                        else:
                            telefone = telefoneVal 
            
            #inserção de email
            email = input("insira o novo email do cliente ou Enter para manter o mesmo: ")

            #insere os dados validados no BD
            clientAlter = Cliente (cpf, nome, endereco_res, telefone, email)
            Cliente.alter_client("LP2Final.db", clientAlter)
            
            #mostra o cliente alterado
            resultado = Cliente.show_client_nome("LP2Final.db", clientAlter)             
            for r in resultado:
                print("\nCliente: ", r[1],"\n", "cpf:", r[0], "\n", "Endereço:", r[2], "\n", "Telefone:", r[3], "\n", "email:", r[4])
        
        elif choice == '4':
            #inserção de cpf 
            cpfVal = False            
            while cpfVal == False:
                cpfVal = validarCpf(input("Insira o cpf do cliente a ser alterado com 11 dígitos sem pontuação: "))
            else:                             
                clientDelete = Cliente(cpf = cpfVal)
                if Cliente.show_client_cpf("LP2Final.db", clientDelete) == []:
                    cpfVal = False
                    print("Cliente não está cadastrado.")
                else:                
                    Cliente.delete_client("LP2Final.db", clientDelete)
                    print("Cliente foi removido da base de dados.")  

        elif choice == '0':            
            cont = False
        else:
            print("Por favor, escolha uma opção de 1 a 4, ou 0 para sair")  
