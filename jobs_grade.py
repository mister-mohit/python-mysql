from connector import *
from applications import *
from mysql.connector import Error

try:

    # table name
    table_name = "job_grade"

    # create table query
    create_table_query = """
        CREATE TABLE {} (
            grade_level VARCHAR(5),
            lowest_sal INT,
            highest_sal INT
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    # insert query
    query = """
        INSERT INTO {}
        (grade_level, lowest_sal, highest_sal)
        VALUES (%s, %s, %s)
    """.format(table_name)

    # values
    values = [

        ("A", 1000, 2999),

        ("B", 3000, 5999),

        ("C", 6000, 9999),

        ("D", 10000, 14999),

        ("E", 15000, 24999),

        ("F", 25000, 40000)

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