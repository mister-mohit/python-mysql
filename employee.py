from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "employee"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            employeeid varchar(100),
            name varchar(100),
            sales integer,
            jobid integer
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (employeeid,name,sales,jobid) VALUES (%s, %s, %s, %s)".format(table_name)

    # change values array
    values = [

("E1","sumit sinha",110000,102),
("E2","vijay singh tomar",130000,101),
("E3","ajay rajpal",140000,103),
("E4","mohit ramanan",125000,102),
("E5","shalija singh",145000,103)
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