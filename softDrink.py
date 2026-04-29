from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "softdrink"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            drinkcode INTEGER,
            dname VARCHAR(100),
            price  FLOAT,
            calories INTEGER
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (drinkcode, dname, price, calories) VALUES (%s, %s, %s, %s)".format(table_name)

    # change values array
    values = [
    (101, "Lime and Lemon", 20.00, 120),
    (102, "Apple Drink", 18.00, 120),
    (103, "Nature Nectar", 15.00, 115),
    (104, "Green Mango", 15.00, 140),
    (105, "Aam Panna", 20.00, 135),
    (106, "Mango Juice Bahaar", 12.0, 150)

    ]



    cursor.executemany(query, values)

    mycon.commit()
    print(cursor.rowcount, "records inserted") 
except Error as err:
    print("Error:", err)
# except Exception as e:
#     print(e)

finally:
    cursor.close()
    mycon.close()

