from connector import *
from applications import *
from mysql.connector import Error

try:

    # table name
    table_name = "countries"

    # create table query
    create_table_query = """
        CREATE TABLE {} (
            country_id VARCHAR(10),
            country_name VARCHAR(100),
            region_id INT
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    # insert query
    query = """
        INSERT INTO {}
        (country_id, country_name, region_id)
        VALUES (%s, %s, %s)
    """.format(table_name)

    # values
    values = [

        ("AR", "Argentina", 2),

        ("AU", "Australia", 3),

        ("BE", "Belgium", 1),

        ("BR", "Brazil", 2),

        ("CA", "Canada", 2),

        ("CH", "Switzerland", 1),

        ("CN", "China", 3),

        ("DE", "Germany", 1),

        ("DK", "Denmark", 1),

        ("EG", "Egypt", 4),

        ("FR", "France", 1),

        ("IL", "Israel", 4),

        ("IN", "India", 3),

        ("IT", "Italy", 1),

        ("JP", "Japan", 3),

        ("KW", "Kuwait", 4),

        ("ML", "Malaysia", 3),

        ("MX", "Mexico", 2),

        ("NG", "Nigeria", 4),

        ("NL", "Netherlands", 1),

        ("SG", "Singapore", 3),

        ("UK", "United Kingdom", 1),

        ("US", "United States of America", 2),

        ("ZM", "Zambia", 4),

        ("ZW", "Zimbabwe", 4)

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