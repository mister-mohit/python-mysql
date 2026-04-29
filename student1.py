from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "student1"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            no integer,
            name varchar(100),
            stipend float,
            stream varchar(100),
            avgmark decimal(10,2),
            grade varchar(100),
            class varchar(50)
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (no,name,stipend,stream,avgmark,grade,class) VALUES (%s, %s, %s, %s,%s, %s, %s)".format(table_name)

    # change values array
    values = [
    
(1,"Karan",400.00,"Medical",78.5,"B","12B"),
(2,"Divakar",450.00,"Commerce",89.2,"A","11C"),
(3,"Divya",300.00,"Commerce",68.6,"C","12C"),
(4,"Arun",350.00,"Humanities",73.1,"B","12C"),
(5,"Sabina",500.00,"Nonmedical",90.6,"A","11A"),
(6,"John",400.00,"Medical",75.4,"B","12B"),
(7,"Robert",250.00,"Humanities",64.4,"C","11A"),
(8,"Rubina",450.00,"Nonmedical",88.5,"A","12A"),
(9,"Vikas",500.00,"Nonmedical",92.0,"A","12A"),
(10,"Mohan",300.00,"Commerce",67.5,"C","12C")
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