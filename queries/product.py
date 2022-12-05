import sqlite3
from sqlite3 import Error

class Produto:
  def __init__(self, idProduto = None, nome = None, fornecedor = None , descricao = None, preco = None, largura = None, altura = None, profundidade = None, peso = None, quantidade = None, frag = None):

    self.idProduto = idProduto
    self.nome = nome
    self.fornecedor = fornecedor
    self.descricao = descricao
    self.preco = preco
    self.largura = largura
    self.altura = altura
    self.profundidade = profundidade
    self.peso = peso
    self.quantidade = quantidade
    self.frag = frag

#Cadastra novo produto no banco de dados
  def new_product(db_file, productNew):    

      #conecta ao banco de dados e insere os dados do novo produto
      conn = None
      try:                 
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
                 
          #insere os dados validados e formatados          
          sql_stmt = "INSERT INTO produto (nome, fornecedor, descricao, preco, largura, altura, profundidade, peso, quantidade, frag) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10);"
          c.execute(sql_stmt, (productNew.nome, productNew.fornecedor, productNew.descricao, productNew.preco, productNew.largura, productNew.altura, productNew.profundidade, productNew.peso, productNew.quantidade, productNew.frag))
          conn.commit()    
          result = c.execute("SELECT * FROM produto;")
          return(c.fetchall())

      except sqlite3.IntegrityError as i:
        print("\nJá existe produto cadastrado com este id! Selecione outra opção ou tente novamente.\n")
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()

  def show_product_nome (db_file, productShow):
    #conecta ao banco de dados e mostra dos dados de um produto
     conn = None
     try:
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
          result = c.execute("SELECT * FROM produto WHERE nome LIKE ? || '%';", (productShow.nome,))           
          return(c.fetchall())
     except Error as e:
          print(e)
     finally:
          if conn:
            conn.close()

  def show_product_id (db_file, productShow):
        #conecta ao banco de dados e mostra dos dados de um cliente
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            c = conn.cursor()            
            result = c.execute("SELECT * FROM produto WHERE idProduto LIKE ? || '%';", (productShow.idProduto,))           
            return(c.fetchall())
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
  
  def alter_product(db_file, productAlter):
        #conecta ao banco de dados e altera os dados de um cliente
      conn = None
      print(productAlter.idProduto)  
      try:
          conn = sqlite3.connect(db_file)
          c = conn.cursor()
          print(productAlter.idProduto)     
          c.execute("SELECT * FROM produto WHERE idProduto = ?", (productAlter.idProduto,))  
          record = c.fetchone()
          if record == None:            
            print("\nProduto não consta da base de dados. Por favor confira o id e tente novamente.\n")
          else:                    
            nomeOld = record [1]
            fornecedorOld = record[2]
            descricaoOld = record[3]
            precoOld  = record[4]
            larguraOld  = record[5]
            alturaOld  = record[6]
            profundidadeOld  = record[7]
            pesoOld  = record[8]
            quantidadeOld  = record[9]
            fragOld  = record[10]            

            if productAlter.nome == "": productAlter.nome = nomeOld
            if productAlter.fornecedor == "": productAlter.fornecedor = fornecedorOld
            if productAlter.descricao == "": productAlter.descricao = descricaoOld
            if productAlter.preco == "": productAlter.preco = precoOld
            if productAlter.largura == "": productAlter.largura = larguraOld
            if productAlter.altura == "": productAlter.altura = alturaOld
            if productAlter.profundidade == "": productAlter.profundidade = profundidadeOld
            if productAlter.peso == "": productAlter.peso = pesoOld
            if productAlter.quantidade == "": productAlter.quantidade = quantidadeOld
            if productAlter.frag == "": productAlter.frag = fragOld
            
            sql_stmt = "UPDATE produto SET nome = ?, fornecedor = ?, descricao = ?, preco = ?, largura = ?, altura = ?, profundidade = ?, peso = ?, quantidade = ?, frag = ? WHERE idProduto = ?"
            c.execute(sql_stmt, (productAlter.nome, productAlter.fornecedor, productAlter.descricao, productAlter.preco, productAlter.largura, productAlter.altura, productAlter.profundidade, productAlter.peso, productAlter.quantidade, productAlter.frag, productAlter.idProduto))          
            conn.commit()          
            return(c.fetchall())
      except sqlite3.TypeError as i:
          print("\nNão existe produto cadastrado com este id! Selecione outra opção ou tente novamente.\n")
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()  