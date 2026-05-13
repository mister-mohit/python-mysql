from connector import *
from applications import *
from mysql.connector import Error

try:

    # table name
    table_name = "job_history"

    # create table query
    create_table_query = """
        CREATE TABLE {} (
            employee_id INT,
            start_date DATE,
            end_date DATE,
            job_id VARCHAR(50),
            department_id INT
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    # insert query
    query = """
        INSERT INTO {}
        (employee_id, start_date, end_date, job_id, department_id)
        VALUES (%s, %s, %s, %s, %s)
    """.format(table_name)

    # values
    values = [

        (102, "2001-01-13", "2006-07-24", "IT_PROG", 60),

        (101, "1997-09-21", "2001-10-27", "AC_ACCOUNT", 110),

        (101, "2001-10-28", "2005-03-15", "AC_MGR", 110),

        (201, "2004-02-17", "2007-12-19", "MK_REP", 20),

        (114, "2006-03-24", "2007-12-31", "ST_CLERK", 50),

        (122, "2007-01-01", "2007-12-31", "ST_CLERK", 50),

        (200, "1995-09-17", "2001-06-17", "AD_ASST", 90),

        (176, "2006-03-24", "2006-12-31", "SA_REP", 80),

        (176, "2007-01-01", "2007-12-31", "SA_MAN", 80),

        (200, "2002-07-01", "2006-12-31", "AC_ACCOUNT", 90)

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