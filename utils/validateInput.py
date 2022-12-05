import string
import numbers
import re
from queries.product import Produto
from queries.pedido import Pedido

#validar cpf
def validarCpf(cpfVal):
   
    if len(cpfVal) != 11:
        print("Número de dígitos incorreto!") 
        return False                      
    else:
        try:
            digitos = list(map(int, cpfVal))
        except ValueError:
            print("Dados incorretos!")
            return False

        def calcula_digito(multiplicador):
            total = 0
            for d in digitos:
                if multiplicador >= 2:
                    total += d * multiplicador
                    multiplicador -= 1
                else:
                    break

            resto = total % 11
            if resto < 2:
                return 0
            else:
                return 11 - resto

        #primeiro digito nao bate, CPF inválido
        if digitos[9] != calcula_digito(10):
            print ("Cpf não é válido! 1")
            return False

        #segundo digito não bate, CPF inválido
        if digitos[10] != calcula_digito(11):
            print ("Cpf não é válido! 2")
            return False
        else:
            return cpfVal
     

def formatarUpper(textFor):
    return textFor.upper()    

def validarTel(telVal):
    if len(telVal) < 10 or len(telVal) >12:
        print("Número de dígitos incorreto!") 
        return False                      
    else:
        return int(re.sub("[^0-9]", "",telVal))

def validarPosFloat(posFloat):
    try:
        if float(posFloat) < 0:
            print("Não é possível atribuir valor negativo!") 
            return -1                     
        else:
            return format(float(posFloat), '.2f')
    except ValueError:
        print ("O valor inserido não é um número!")
        return -1

def validarPosInt(posInt):
    try:
        if int(posInt) < 0:
            print("Não é possível atribuir valor negativo!") 
            return -1                      
        else:
            return int(posInt)
    except ValueError:
        print ("O valor inserido não é um número!")
        return -1

def validaSN(SN):
    
    if SN == "S" or SN == "s":       
        return "Sim"             
    elif SN == "N" or SN == "n":     
        return "Não"        
    else:
        print("Por favor, responda (S)im ou (N)ão.")
        return False

def validarID (idVal):
    try:
        id = int(idVal)        
        return idVal
    except:        
        productShow = Produto(nome = idVal)        
        resultado = Produto.show_product_nome("LP2Final.db", productShow)                   
        if resultado == []:
            print("\nNão existem produtos com este nome (parcial ou total).\n")
            
        else:
            for r in resultado:
                print("\nProduto: ", r[1],"\n", "id:", r[0], "\n", "Fornecedor:", r[2], "\n", "Descrição:", r[3], "\n", "preço:", r[4], "\n", "Largura", r[5], "\n", "Altura:", r[6], "\n", "Profundidade:", r[7], "\n", "Peso:", r[8], "\n", "Quantidade em estoque:", r[9], "\n", "É frágil? ", r[10], "\n")
        return -1   

def validarIDPedido (idVal):
    try:
        id = int(idVal)        
        return idVal
    except:        
        orderShow = (idVal,0)        
        resultado = Pedido.show_order_nome("LP2Final.db", orderShow)                   
        if resultado == []:
            print("\nNão existem pedidos no nome deste cliente (parcial ou total).\n")
            
        else:
            for r in resultado:
                print("\nCliente: ", r[1],"\n", "id:", r[0], "\n", "Endereço de entrega ", r[2], "\n")
        return-1 