import sqlite3
from sqlite3 import Error

class Cliente:
  def __init__(self, cpf = None, nome = None, endereco_res = None, telefone = None, email = None):
    self.cpf = cpf
    self.nome = nome
    self.endereco_res = endereco_res
    self.telefone = telefone
    self.email = email

#Cadastra novo cliente no banco de dados
  def new_client(db_file, clientNew):    

      #conecta ao banco de dados e insere os dados do novo cliente
      conn = None
      try:                 
          conn = sqlite3.connect(db_file)
          c = conn.cursor()         
          
          sql_stmt = "INSERT INTO cliente (cpf, nome, endereco, telefone, email) VALUES (?, ?, ?, ?, ?)"
          c.execute(sql_stmt, (clientNew.cpf, clientNew.nome, clientNew.endereco_res, clientNew.telefone, clientNew.email))
          conn.commit()    
          #result = c.execute("SELECT * FROM cliente;")
          return(c.fetchall())
      except sqlite3.IntegrityError as i:
        print("\nJá existe cliente cadastrado com este cpf! Selecione outra opção ou tente novamente.\n")
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()

  def show_client_nome (db_file, clientShow):
    #conecta ao banco de dados e mostra dos dados de um cliente
     conn = None
     try:
          conn = sqlite3.connect(db_file)
          c = conn.cursor() 
          c.execute("SELECT * FROM cliente WHERE nome LIKE ? || '%'", (clientShow.nome,))
          return(c.fetchall())           
          
     except Error as e:
          print(e)
     finally:
          if conn:
            conn.close()

  def show_client_cpf (db_file, clientShow):
        #conecta ao banco de dados e mostra dos dados de um cliente
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            c = conn.cursor() 
            c.execute("SELECT * FROM cliente WHERE cpf LIKE ? || '%'", (clientShow.cpf,))  
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