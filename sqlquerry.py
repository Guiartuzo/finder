import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sql_inventory',
                                         user='root',
                                         password='adminadmin123')

    sql_select_Query = "select * from products"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in products is: ", cursor.rowcount)

    print("\nPrinting each products record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("quantity in stock  = ", row[2])
        print("price   = ", row[3], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()67890-/*
        cursor.close()
        print("MySQL connection is closed")