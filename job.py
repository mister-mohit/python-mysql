from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "job"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            jobid integer,
            jobtitle varchar(100),
            salary integer
            
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (jobid,jobtitle,salary) VALUES (%s, %s, %s)".format(table_name)

    # change values array
    values = [

(101,"president",200000),
(102,"vice president",125000),
(103,"administration assistant",80000),
(104,"accounting manager",70000),
(105,"accountant",65000),
(106,"sales manager",80000)
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