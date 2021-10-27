import mysql.connector
from credentials import usr, pswd

def insert_db(idCaptura, computador, fkTorre, usuario, cpu, mem, disco, internet):
    try:  
        mydb = mysql.connector.connect(
            host = "localhost",
            user = usr,
            password = pswd,
            database = "towerTech"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor() # mandar query para o MySQL

            sql_query = "INSERT INTO tbCapturaDeDados() VALUES (%s, %s, %s, %s, %s, %s, %s, %s,now())"
            val = [idCaptura, computador, fkTorre, usuario, cpu, mem, disco, internet]
            mycursor.execute(sql_query, val)
            
            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")

def selectbanco():
    cnx = mysql.connector.connect(user=usr, password=pswd, database='towertech')
    cursor = cnx.cursor()

    query = ("SELECT * FROM TBEMPRESAS")


    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    
    
    # for row in records:
    #     print("Id = ", row[0])

    cursor.close()
    cnx.close()
