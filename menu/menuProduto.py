from queries.product import Produto
from utils.validateInput import validarCpf, formatarUpper, validarTel, validarPosFloat, validarPosInt, validaSN, validarID
        
def productMenu():
    cont = True   
    while cont == True:
        choice = input("Selecione a opção desejada:\n\n[1] - Consultar todos os produtos ou procurar por nome.\n[2] - Cadastrar novo produto.\n[3] - Alterar dados de um produto existente.\n[0] - Voltar ao Menu principal.\n")

        #consulta produto
        if choice == '1':
            #Verificaçao de dados de um produto:
             
             nome = input("Insira o nome do produto a ser consultado, ou enter para ver todos: ")
             productShow = Produto(nome = nome)
             resultado = Produto.show_product_nome("LP2Final.db", productShow)             
             if resultado == []:
                print("\nNão existem produtos com este nome (parcial ou total).\n")
             else:
                for r in resultado:
                 print("\nProduto: ", r[1],"\n", "id:", r[0], "\n", "Fornecedor:", r[2], "\n", "Descrição:", r[3], "\n", "preço:", r[4], "\n", "Largura", r[5], "\n", "Altura:", r[6], "\n", "Profundidade:", r[7], "\n", "Peso:", r[8], "\n", "Quantidade em estoque:", r[9], "\n", "É frágil? ", r[10], "\n")

        #insere novo produto
        elif choice == '2':                   

            #inserção de nome
            nome = formatarUpper(input("Insira o nome do produto: "))
                       
            #inserção de fornecedor
            fornecedor = formatarUpper(input("Insira o nome do fornecedor do produto: "))

            #inserção de descrição
            descricao = formatarUpper(input("Insira a descrição do produto: "))

            #inserção de preço
            precoVal = -1
            while precoVal == -1:
                precoVal = validarPosFloat(input("Insira o preço do produto: "))             
            else:
                preco = precoVal              

            #inserção de largura
            largVal = -1
            while largVal == -1:
                largVal = validarPosFloat(input("Insira a largura do produto: "))             
            else:
                largura = largVal             

            #inserção de altura
            altVal = -1
            while altVal == -1:
                altVal = validarPosFloat(input("Insira a altura do produto: "))             
            else:
                altura = altVal  
            
            #inserção de profundidade
            profVal = -1
            while profVal == -1:
                profVal = validarPosFloat(input("Insira a profundidade do produto: "))           
            else:
                profundidade = profVal            

            #inserção de peso
            pesoVal = -1
            while pesoVal == -1:
                pesoVal = validarPosFloat(input("Insira o peso do produto: "))              
            else:
                peso = pesoVal              

            #inserção de quantidade em estoque
            quantVal = -1
            while quantVal == -1:
                quantVal = validarPosInt(input("Insira o quantidade em estoque do produto: "))              
            else:
                quant = quantVal             

            #inserção de fragilidade
            fragVal = False
            while fragVal == False:
                fragVal = validaSN(input("O produto é frágil (S/N)? "))               
            else:
                frag = fragVal 
                      
            #insere os dados validados no BD
            productNew = Produto (None, nome, fornecedor, descricao, preco, largura, altura, profundidade, peso, quant, frag)
            Produto.new_product("LP2Final.db", productNew)
            
            resultado = Produto.show_product_nome("LP2Final.db", productNew)             
            for r in resultado:
                 print("\nProduto: ", r[1],"\n", "id:", r[0], "\n", "Fornecedor:", r[2], "\n", "Descrição:", r[3], "\n", "preço:", r[4], "\n", "Largura", r[5], "\n", "Altura:", r[6], "\n", "Profundidade:", r[7], "\n", "Peso:", r[8], "\n", "Quantidade em estoque:", r[9], "\n", "É frágil? ", r[10], "\n")

        #altera produto existente    
        elif choice == '3':
            #inserção de id 
            idVal = -1          
            while idVal == -1:
                idVal = validarID(input("Insira o id do produto a ser alterado ou escreva o nome do produto para consultar (enter para exibir todos): "))
            else:
                idProduto = idVal                                       
            
            #inserção de nome
            nome = formatarUpper(input("Insira o novo nome do produto ou Enter para manter o mesmo: "))
                       
           #inserção de fornecedor
            fornecedor = formatarUpper(input("Insira o novo fornecedor do produto: "))

            #inserção de descrição
            descricao = formatarUpper(input("Insira a nova descrição do produto: "))

            #inserção de preço
            precoVal = -1
            while precoVal == -1:
                precoVal = input("Insira o preço do produto: ") 
                match precoVal:
                    case "":
                        preco = ""                      
                    case _:
                        if validarPosFloat(precoVal) == -1:
                            precoVal = -1
                        else:
                            preco = precoVal
            
            #inserção de largura
            larguraVal = -1
            while larguraVal == -1:
                larguraVal = input("Insira a nova largura do produto: ")
                match larguraVal:
                    case "":
                        largura = ""                      
                    case _:
                        if validarPosFloat(larguraVal) == -1:
                            larguraVal = -1
                        else:
                            largura = larguraVal
            

            #inserção de altura
            alturaVal = -1
            while alturaVal == -1:
                alturaVal = input("Insira a nova altura do produto: ")
                match alturaVal:
                    case "":
                        altura = ""                      
                    case _:
                        if validarPosFloat(alturaVal) == -1:
                            alturaVal = -1
                        else:
                            altura = alturaVal            

            #inserção de profundidade
            profundidadeVal = -1
            while profundidadeVal == -1:
                profundidadeVal = input("Insira a nova profundidade do produto: ")
                match profundidadeVal:
                    case "":
                        profundidade = ""                      
                    case _:
                        if validarPosFloat(profundidadeVal) == -1:
                            profundidadeVal = -1
                        else:
                            profundidade = profundidadeVal             

            #inserção de peso
            pesoVal = -1
            while pesoVal == -1:
                pesoVal = input("Insira o novo peso do produto: ")
                match pesoVal:
                    case "":
                        peso = ""                      
                    case _:
                        if validarPosFloat(pesoVal) == -1:
                            pesoVal = -1
                        else:
                            peso = pesoVal            

            #inserção de quantidade em estoque
            quantVal = -1
            while quantVal == -1:
                quantVal = input("Insira a nova quantidade em estoque do produto: ")
                match quantVal:
                    case "":
                        quant = ""                      
                    case _:
                        if validarPosFloat(quantVal) == -1:
                            quantVal = -1
                        else:
                            quant = quantVal            

            #inserção de fragilidade            
            fragVal = False
            while fragVal == False:
                fragVal = validaSN(input("O produto é frágil (S/N)? "))               
            else:
                frag = fragVal

            #insere os dados validados no BD
            productAlter = Produto (idProduto, nome, fornecedor, descricao, preco, largura, altura, profundidade, peso, quant, frag)
            Produto.alter_product("LP2Final.db", productAlter)
            
            #mostra o cliente alterado
            resultado = Produto.show_product_id("LP2Final.db", productAlter)             
            for r in resultado:
                print("\nProduto: ", r[1],"\n", "id:", r[0], "\n", "Fornecedor:", r[2], "\n", "Descrição:", r[3], "\n", "preço:", r[4], "\n", "Largura", r[5], "\n", "Altura:", r[6], "\n", "Profundidade:", r[7], "\n", "Peso:", r[8], "\n", "Quantidade em estoque:", r[9], "\n", "É frágil? ", r[10], "\n")
        
        #Retorna ao menu principal
        elif choice == '0':            
            cont = False

        #caso digite opção inválida
        else:
            print("Por favor, escolha uma opção de 1 a 3, ou 0 para sair")  
