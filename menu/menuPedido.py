from queries.pedido import Pedido
from queries.product import Produto
from utils.validateInput import validarCpf, formatarUpper, validarIDPedido, validarID, validarPosInt
from functools import reduce
        
def orderMenu():
    cont = True   
    while cont == True:
        choice = input("Selecione a opção desejada:\n\n[1] - Consultar todos os pedidos ou procurar por nome do cliente.\n[2] - Cadastrar novo pedido.\n")

        #consulta pedido
        if choice == '1':
            #Verificaçao de dados de um pedido:

             idVal = -1          
             while idVal == -1:
                idVal = validarIDPedido(input("Insira o id do pedido a ser consultado, ou insira o nome do cliente a ser consultado (enter para exibir todos): "))
             else:
                idPedido = idVal
                ordershow = (idVal)
                #envia os dados e captura o id do pedido recém criado
                resultado = Pedido.show_pedido_id("LP2Final.db", ordershow)
                print (resultado)
             
                if resultado == []:
                    print("\nNão existem pedido com este id.\n")           
                else:
                    print(f"\nCliente: {resultado[0][1]}\n")
                    partials = []
                    for r in resultado:                    
                       print(f"id Produto: {r[3]}\nNome produto: {r[4]}\nPreço unitário produto: R${r[5]:.2f}\nQuantidade: {r[6]}\nValor total do item: R${r[5]*r[6]:.2f}\n")
                       partials.append(r[5]*r[6])
                       print(f"Valor total do pedido: R${reduce(lambda acc, current:acc + current, partials, 0):.2f}\n")

        #insere novo pedido
        elif choice == '2':

            #criação do pedido

            #inserção de cpf 
            cpfVal = False            
            while cpfVal == False:
                cpfVal = validarCpf(input("Insira o cpf do cliente com 11 dígitos sem pontuação: "))
            else:
                cpf = cpfVal              
                                  
            #inserção de endereço de entrega
            endereco_entrega = formatarUpper(input("Insira o endereço de entrega do pedido: "))
            
           
            #insere os dados validados no BD            
            orderNew = Pedido (None, cpf, endereco_entrega)
            #envia os dados e captura o id do pedido recém criado
            idPed = Pedido.new_order("LP2Final.db", orderNew)
            print (idPed)
            
            #resultado = Cliente.show_client_nome("LP2Final.db", clientNew)             
            #for r in resultado:
            #    print("\nCliente: ", r[1],"\n", "cpf:", r[0], "\n", "Endereço:", r[2], "\n", "Telefone:", r[3], "\n", "email:", r[4])

            #inserção de produtos no pedido

            adicionaProduto = 1
            while adicionaProduto == 1:
                idPedido = idPed

                #inserção de id 
                idVal = -1          
                while idVal == -1:
                    idVal = validarPosInt(input("Insira o id do produto a ser adicionado ao pedido ou escreva o nome do produto para consultar (enter para exibir todos).\nInsira 0 para finalizar a inserção de produtos: "))
                    if idVal == 0:
                        print("Pedido Finalizado!")
                        adicionaProduto = -1                                               
                    
                else:
                    idProduto = idVal
                    productShow = Produto (idProduto)
                    resultado = Produto.show_product_id("LP2Final.db", productShow)             
                    for r in resultado:                        
                        print ("Há ", r[9], "unidades do produto ", r[1], "em estoque.\n")
                        quantVal = -1                     
                        
                        while quantVal == -1:
                            quantVal = input ("Quantas unidades devem ser adicionadas ao produto? ")
                            quantVal = validarPosInt(quantVal)
                            if quantVal > r[9]:
                                print ("Não há peças suficientes em estoque!")
                                quantVal = -1
                            elif quantVal == 0:
                                idVal = 0                                
                            else:
                                quantFinal = r[9] - quantVal
                                print(quantFinal)
                                quant = quantVal
                                prodOrderNew = (idPedido, idProduto, quant, quantFinal)
                                print (quant)
                                Pedido.new_product_in_order("LP2Final.db", prodOrderNew)  
        #Retorna ao menu principal
        elif choice == '0':            
            cont = False

        #caso digite opção inválida
        else:
            print("Por favor, escolha uma opção de 1 ou 2, ou 0 para sair")                      