import sqlite3
from sqlite3 import Error

def create_tables(db_file):
    #conecta ao banco de dados
      conn = None
      try:                 
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
        
          #cria as tabelas se não existirem
          c.execute ('''CREATE TABLE IF NOT EXISTS cliente (cpf INTEGER PRIMARY KEY UNIQUE, nome TEXT, endereco TEXT, telefone INT, email TEXT);''')       
          conn.commit()
          c.execute ('''CREATE TABLE IF NOT EXISTS produto (idProduto INTEGER PRIMARY KEY UNIQUE, nome TEXT, fornecedor TEXT, descricao TEXT, preco FLOAT, largura FLOAT, altura FLOAT, profundidade FLOAT, peso FLOAT, quantidade INT, frag TEXT);''')
          conn.commit()  
          c.execute ('''CREATE TABLE IF NOT EXISTS pedido (idPedido INTEGER PRIMARY KEY UNIQUE, comprador TEXT, endereco_entrega TEXT);''')
          conn.commit()
          c.execute ('''CREATE TABLE IF NOT EXISTS produto_no_pedido (idPedido INTEGER NOT NULL, idProduto INTEGER NOT NULL, preco FLOAT, quantidade INTEGER, FOREIGN KEY (idPedido) REFERENCES pedido(idPedido), FOREIGN KEY (idProduto) REFERENCES produto(idProduto), PRIMARY KEY (idPedido, idProduto));''')
          conn.commit()         

      #gerenciamento de erros
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close() 

def delete_tables(db_file):    
          
      #conecta ao banco de dados 
      conn = None
      try:                 
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
        
          #deleta as tabelas se existirem
          c.execute ("DROP TABLE IF EXISTS cliente;") 
          conn.commit()  
          c.execute ("DROP TABLE IF EXISTS produto;") 
          conn.commit() 
          c.execute ("DROP TABLE IF EXISTS pedido;") 
          conn.commit() 
          c.execute ("DROP TABLE IF EXISTS produto_no_pedido;") 
          conn.commit()        

      #gerenciamento de erros
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close() 