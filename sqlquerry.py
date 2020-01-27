import mysql.connector
from mysql.connector import Error   

def getMaterial(idtest,id):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='smartlab',
                                            user='root',
                                            password='adminadmin123')

        cursor = connection.cursor(buffered=True)
        sql_select_Query = """SELECT * FROM materiais WHERE %s = %s ORDER BY id_material"""
        cursor.execute(sql_select_Query,(idtest,id))
        records = cursor.fetchall()

        print("\nFetching itens...")
        for row in records:
            print("The selected product name is =  ", row[3], "\n")
            print("Quantity = ", row[4], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()   
            cursor.close()
            print("MySQL connection is closed")

id1 = "familia"
id2 = "solda"
getMaterial(id1,id2)