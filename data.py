from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "data"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            rollno integer,
            name varchar(100),
            marks decimal(10,2),
            grade varchar(100),
            section varchar(100),
            project varchar(50)
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (rollno,name,marks,grade,section,project) VALUES (%s, %s, %s, %s,%s, %s)".format(table_name)

    # change values array
    values = [

(101,"Ruhani",76.80,"A","A","Pending"),
(102,"George",71.20,"B","A","Submitted"),
(103,"Simran",81.20,"A","B","Evaluated"),
(104,"Ali",61.20,"B","C","Assigned"),
(105,"Kushal",51.60,"C","C","Evaluated"),
(106,"Arsiya",91.60,"A+","B","Submitted"),
(107,"Raunaq",32.50,"F","B","Submitted"),
(108,"Meera",97.20,"A+","B","Evaluated"),
(109,"Amaal",57.20,"C","A","Pending"),
(111,"Simran",66.00,"B","A","Pending"),
(112,"Adam",74.00,"B","C","Pending"),
(113,"Gurnoor",93.50,"A+","B","Assigned"),
(115,"Rabiya",72.50,"B","B","Assigned"),
(117,"Rahil",32.00,"F","C","Submitted"),
(118,"Neha",59.50,"C","A","Evaluated")
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