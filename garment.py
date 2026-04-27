from connector import *
from applications import *

try:

    table_name = "garments"
    create_table_query = """
        CREATE TABLE {} (
            gcode INT,
            gname VARCHAR(100),
            size  VARCHAR(5),
            colour VARCHAR(100),
            price DECIMAL
        )
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    # SQL query
    query = "INSERT INTO {} (gcode, gname, size, colour, price) VALUES (%s, %s, %s, %s, %s)".format(table_name)

    # multiple records (list of tuples)
    values = [
        (111, "TShirt", "XL", "Red", 1400.00),
        (112, "Jeans", "L", "Blue", 1600.00),
        (113, "Skirt", "M", "Black", 1100.00),
        (114, "Ladies Jacket", "Blue", "Red", 4000.00),
        (115, "Trousers", "L", "Brown", 1500.00),
        (116, "Ladies Top", "L", "Pink", 1200.00),
    ]

    # execute multiple insert
    cursor.executemany(query, values)

    mycon.commit()
    print(cursor.rowcount, "records inserted") 
except Exception as e:
    print(e)
finally:
    cursor.close()
    mycon.close()


# # Create table query
# create_table_query = """
# CREATE TABLE students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     age INT,
#     email VARCHAR(100)
# )
# """

# # Execute query
# cursor.execute(create_table_query)
# print("Table created successfully!")

# # SQL query
# query = "INSERT INTO students (gcode, gname, size, colour, price) VALUES (%s, %s, %s, %s, %s)"

# # multiple records (list of tuples)
# values = [
#     (111, "TShirt", "XL", "Red", 1400.00),
#     (112, "Jeans", "L", "Blue", 1600.00),
#     (113, "Skirt", "M", "Black", 1100.00),
#     (114, "Ladies Jacket", "Blue", "Red", 4000.00),
#     (115, "Trousers", "L", "Brown", 1500.00),
#     (116, "Ladies Top", "L", "Pink", 1200.00),
# ]

# # execute multiple insert
# cursor.executemany(query, values)

# # commit changes
# mycon.commit()

# print(cursor.rowcount, "records inserted")

