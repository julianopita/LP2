import sqlite3
from sqlite3 import Error

class Pedido:
  def __init__(self, idPedido = None, cpf = None, endereco_entrega = None):
    self.idPedido = idPedido
    self.cpf = cpf
    self.endereco_entrega = endereco_entrega    

#Cadastra novo pedido no banco de dados
  def new_order(db_file, orderNew):    

      #conecta ao banco de dados e insere os dados do novo pedido
      conn = None
      try:                 
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
    
          sql_stmt = "INSERT INTO pedido (comprador, endereco_entrega) SELECT cliente.nome, ? FROM cliente WHERE cpf = ?"          
          c.execute(sql_stmt, (orderNew.endereco_entrega, orderNew.cpf))
          conn.commit()
          return(c.lastrowid)

      except sqlite3.IntegrityError as i:
        print("\nJá existe pedido cadastrado com este id! Selecione outra opção ou tente novamente.\n")
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()

  def new_product_in_order(db_file, prodOrderNew):    

      #conecta ao banco de dados e insere os dados do novo produto no pedido
      conn = None
      try:                 
          conn = sqlite3.connect(db_file)
          c = conn.cursor()

          sql_stmt = "UPDATE produto SET quantidade = ? WHERE idProduto = ?"          
          c.execute(sql_stmt, (prodOrderNew[3], prodOrderNew[1]))                   
          
          sql_stmt = "INSERT INTO produto_no_pedido (idPedido, idProduto, preco, quantidade) SELECT ?, ?, produto.preco, ? FROM produto WHERE idProduto = ?"
          
          c.execute(sql_stmt, (prodOrderNew[0], prodOrderNew[1], prodOrderNew[2], prodOrderNew[1]))
          conn.commit()
          return(c.fetchall())

      except sqlite3.IntegrityError as i:
        print("\nJá existe pedido cadastrado com este id! Selecione outra opção ou tente novamente.\n")
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()

  def show_order_nome (db_file, orderShow):
    #conecta ao banco de dados e mostra dos dados de um cliente
     conn = None
     try:
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
          c.execute("SELECT * FROM pedido WHERE comprador LIKE ? || '%'", (orderShow[0],))
          return(c.fetchall())           
          
     except Error as e:
          print(e)
     finally:
          if conn:
            conn.close()

  def show_pedido_id (db_file, orderShow):
    #conecta ao banco de dados e mostra dos dados de um cliente
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()            
        result = c.execute("SELECT pedido.idPedido, pedido.comprador, pedido.endereco_entrega, produto_no_pedido.idProduto, produto.nome, produto_no_pedido.preco, produto_no_pedido.quantidade FROM pedido INNER JOIN produto_no_pedido ON pedido.idPedido = produto_no_pedido.idPedido INNER JOIN produto ON produto_no_pedido.idProduto = produto.idProduto WHERE pedido.idPedido = ?;", (orderShow[0],))           
        return(c.fetchall())
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
  
  def alter_client(db_file, clientAlter):
        #conecta ao banco de dados e altera os dados de um cliente
      conn = None
      try:
          conn = sqlite3.connect(db_file)
          c = conn.cursor()   
          c.execute("SELECT * FROM cliente WHERE cpf = ?", (clientAlter.cpf,))
          record = c.fetchone()

          if record == None:            
            print("\nCliente não consta da base de dados. Por favor confira o cpf e tente novamente.\n")
          else:
            nomeOld = record[1]
            endereco_resOld = record [2]
            telefoneOld = record [3]
            emailOld = record [4]

            if clientAlter.nome == "": clientAlter.nome = nomeOld
            if clientAlter.endereco_res == "": clientAlter.endereco_res = endereco_resOld
            if clientAlter.telefone == "": clientAlter.telefone = telefoneOld
            if clientAlter.email == "": clientAlter.email = emailOld
            
            sql_stmt = "UPDATE cliente SET nome = ?, endereco = ?, telefone = ?, email = ? WHERE cpf = ?"
            c.execute(sql_stmt, (clientAlter.nome, clientAlter.endereco_res, clientAlter.telefone, clientAlter.email, clientAlter.cpf))          
            conn.commit()          
            return(c.fetchall())      
      except Error as e:
          print(e)
      finally:
          if conn:
             conn.close()

  def delete_client(db_file, clientDelete):
      
      #conecta ao banco de dados e altera os dados do novo cliente
      conn = None
      try:
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
          
          sql_stmt = "DELETE FROM cliente WHERE cpf = ?"
          c.execute (sql_stmt, (clientDelete.cpf,))
          conn.commit()
          result = c.execute("SELECT * FROM cliente;")
          print(c.fetchall())
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()