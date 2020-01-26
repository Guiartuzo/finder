import mysql.connector
from mysql.connector import Error

def getProductPrice(id):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='sql_inventory',
                                            user='root',
                                            password='adminadmin123')

        cursor = connection.cursor()
        sql_select_Query = """SELECT * FROM products WHERE product_id = %s"""
        cursor.execute(sql_select_Query,(id,))
        records = cursor.fetchall()

        print("\nPrinting price...d")
        for row in records:
            #print("Id = ", row[0], )
            #print("Name = ", row[1])
            #print("quantity in stock  = ", row[2])
            print("The selected product price is =  ", row[3], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()   
            cursor.close()
            print("MySQL connection is closed")

id1 = 2
getProductPrice(id1)