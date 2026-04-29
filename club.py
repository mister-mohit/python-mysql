from connector import *
from applications import *
from mysql.connector import Error

try:

    # change table name
    table_name = "club"
    # change table query
    create_table_query = """
        CREATE TABLE {} (
            coach_id integer,
            coachname varchar(100),
            age integer,
            sports varchar(100),
            dateofapp date,
            pay integer,
            sex varchar(100)
        );
    """.format(table_name)

    createTable(cursor, table_name, create_table_query)

    #change insert query
    query = "INSERT INTO {} (coach_id,coachname,age,sports,dateofapp,pay,sex) VALUES (%s, %s, %s, %s,%s, %s, %s)".format(table_name)

    # change values array
    values = [
    
    (1, "KUKREJA", 35, "KARATE", "1996/03/27", 1000, "M"),
    (2, "RAVINA", 34, "KARATE", "1998/01/20", 1200, "F"),
    (3, "KARAN", 34, "SQUASH", "1998/02/19", 2000, "M"),
    (4, "TARUN", 33, "BASKETBALL", "1998/01/01", 1500, "M"),
    (5, "ZUBIN", 36, "SWIMMING", "1998/01/12", 750, "M"),
    (6, "KETAKI", 36, "SWIMMING", "1998/02/24", 800, "F"),
    (7, "ANKITA", 39, "SQUASH", "1998/02/20", 2200, "F"),
    (8, "ZAREEN", 37, "KARATE", "1998/02/22", 1100, "F"),
    (9, "KUSH", 41, "SWIMMING", "1998/01/13", 900, "M"),
    (10, "SHALIYA", 37, "BASKETBALL", "1998/02/19", 1700, "M")
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