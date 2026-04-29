from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "empl"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            empno INTEGER,
            ename VARCHAR(100),
            job varchar(100),
            mgr integer,
            hiredate date,
            sal float,
            comm float,
            deptno integer
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (empno,ename,job,mgr,hiredate,sal,comm,deptno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(table_name)

    # change values array
    values = [
    (8369, "SMITH", "CLERK", 8902, "1990-12-18", 800.00, None, 20),
    (8499, "ANYA", "SALESMAN", 8698, "1991-02-20", 1600.00, 300.00, 30),
    (8521, "SETH", "SALESMAN", 8698, "1991-02-22", 1250.00, 500.00, 30),
    (8566, "MAHADEVAN", "MANAGER", 8839, "1991-04-02", 2985.00, None, 20),
    (8654, "MOMIN", "SALESMAN", 8698, "1991-09-28", 1250.00, 1400.00, 30),
    (8698, "BINA", "MANAGER", 8839, "1991-05-01", 2850.00, None, 30),
    (8882, "SHIAVNSH", "MANAGER", 8839, "1991-06-09", 2450.00, None, 10),
    (8888, "SCOTT", "ANALYST", 8566, "1992-12-09", 3000.00, None, 20),
    (8839, "AMIR", "PRESIDENT", None, "1991-11-18", 5000.00, None, 10),
    (8344, "KULDEEP", "SALESMAN", 8698, "1991-09-08", 1500.00, 0.00, 30),
    (8886, "ANOOP", "CLERK", 8888, "1993-01-12", 1100.00, None, 20),
    (8900, "JATIN", "CLERK", 8698, "1991-12-03", 950.00, None, 30),
    (8902, "FAKIR", "ANALYST", 8566, "1991-12-03", 3000.00, None, 20),
    (8934, "MITA", "CLERK", 8882, "1992-01-23", 1300.00, None, 10)
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