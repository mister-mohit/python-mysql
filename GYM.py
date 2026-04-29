from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "gym"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            icode VARCHAR(100),
            iname varchar(100),
            price integer,
            brandname varchar(100)
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (icode,iname,price,brandname) VALUES (%s, %s, %s, %s)".format(table_name)

    # change values array
    values = [
    
    ("G101", "Power Fit Exerciser", 20000, "Power Gymrea"),
    ("G102", "Aquafit Hand Grip", 1800, "Reliable"),
    ("G103", "Cycle Bike", 14000, "Ecobike"),
    ("G104", "Protoner Extreme Gym", 30000, "Coscore"),
    ("G105", "Message Belt", 5000, "Message Expert"),
    ("G106", "Cross Trainer", 13000, "GTC Fitness")
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