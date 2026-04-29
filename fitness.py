from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "fitness"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            pcode VARCHAR(100),
            pname varchar(100),
            price integer,
            manufacturer varchar(100)
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (pcode,pname,price,manufacturer) VALUES (%s, %s, %s, %s)".format(table_name)

    # change values array
    values = [
    
    
    ("P1", "Treadmill", 21000, "Coscore"),
    ("P2", "Bike", 20000, "Aone"),
    ("P3", "Cross Trainer", 14000, "Reliable"),
    ("P4", "Multi Gym", 34000, "Coscore"),
    ("P5", "Massage Chair", 5500, "Regrosense"),
    ("P6", "Belly Vibrator Belt", 6500, "Ambhawya")
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