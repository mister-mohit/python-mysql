from connector import *
from applications import *
from mysql.connector import Error

try:

    # table name
    table_name = "jobs"

    # create table query
    create_table_query = """
        CREATE TABLE {} (
            job_id VARCHAR(20),
            job_title VARCHAR(100),
            min_salary INT,
            max_salary INT
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    # insert query
    query = """
        INSERT INTO {}
        (job_id, job_title, min_salary, max_salary)
        VALUES (%s, %s, %s, %s)
    """.format(table_name)

    # values
    values = [

        ("AD_PRES", "President", 20080, 40000),

        ("AD_VP", "Administration Vice President", 15000, 30000),

        ("AD_ASST", "Administration Assistant", 3000, 6000),

        ("FI_MGR", "Finance Manager", 8200, 16000),

        ("FI_ACCOUNT", "Accountant", 4200, 9000),

        ("AC_MGR", "Accounting Manager", 8200, 16000),

        ("AC_ACCOUNT", "Public Accountant", 4200, 9000),

        ("SA_MAN", "Sales Manager", 10000, 20080),

        ("SA_REP", "Sales Representative", 6000, 12008),

        ("PU_MAN", "Purchasing Manager", 8000, 15000),

        ("PU_CLERK", "Purchasing Clerk", 2500, 5500),

        ("ST_MAN", "Stock Manager", 5500, 8500),

        ("ST_CLERK", "Stock Clerk", 2008, 5000),

        ("SH_CLERK", "Shipping Clerk", 2500, 5500),

        ("IT_PROG", "Programmer", 4000, 10000),

        ("MK_MAN", "Marketing Manager", 9000, 15000),

        ("MK_REP", "Marketing Representative", 4000, 9000),

        ("HR_REP", "Human Resources Representative", 4000, 9000),

        ("PR_REP", "Public Relations Representative", 4500, 10500)

    ]

    # insert records
    cursor.executemany(query, values)

    # save changes
    mycon.commit()

    print(cursor.rowcount, "records inserted")

except Error as err:
    print("Error:", err)

finally:
    cursor.close()
    mycon.close()