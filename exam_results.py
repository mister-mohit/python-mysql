from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "exam_results"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            stu_id integer,
            fname varchar(100),
            lname varchar(100),
            exam_id integer,
            exam_score integer
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (stu_id,fname,lname,exam_id,exam_score) VALUES (%s, %s, %s, %s,%s)".format(table_name)

    # change values array
    values = [

(10,"laura","lynch",1,90),  
(10,"laura","lynch",2,85) , 
(11,"grace","brown",1,78)  ,
(11,"grace","brown",2,72)  ,
(12,"jay","jackson",1,95)  ,
(12,"jay","jackson",2,92)  ,
(13,"william","bishop",1,70),  
(13,"william","bishop",2,100),  
(14,"charles","prada",2,85)
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