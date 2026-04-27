def createTable(cursor, table_name, create_table_query):

    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()

    if result:
        raise Exception("Table exists")
    else: 
        cursor.execute(create_table_query)
        print("Table created successfully!")