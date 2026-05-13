from connector import *
from applications import *
from mysql.connector import Error

try:

    # table name
    table_name = "departments"

    # create table query
    create_table_query = """
        CREATE TABLE {} (
            department_id INT,
            department_name VARCHAR(100),
            manager_id INT,
            location_id INT
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    # insert query
    query = """
        INSERT INTO {}
        (department_id, department_name, manager_id, location_id)
        VALUES (%s, %s, %s, %s)
    """.format(table_name)

    # values
    values = [

        (10, "Administration", 200, 1700),

        (20, "Marketing", 201, 1800),

        (30, "Purchasing", 114, 1700),

        (40, "Human Resources", 203, 2400),

        (50, "Shipping", 121, 1500),

        (60, "IT", 103, 1400),

        (70, "Public Relations", 204, 2700),

        (80, "Sales", 145, 2500),

        (90, "Executive", 100, 1700),

        (100, "Finance", 108, 1700),

        (110, "Accounting", 205, 1700),

        (120, "Treasury", 0, 1700),

        (130, "Corporate Tax", 0, 1700),

        (140, "Control And Credit", 0, 1700),

        (150, "Shareholder Services", 0, 1700),

        (160, "Benefits", 0, 1700),

        (170, "Manufacturing", 0, 1700),

        (180, "Construction", 0, 1700),

        (190, "Contracting", 0, 1700),

        (200, "Operations", 0, 1700),

        (210, "IT Support", 0, 1700),

        (220, "NOC", 0, 1700),

        (230, "IT Helpdesk", 0, 1700),

        (240, "Government Sales", 0, 1700),

        (250, "Retail Sales", 0, 1700),

        (260, "Recruiting", 0, 1700),

        (270, "Payroll", 0, 1700)

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