import mysql.connector 
mycon = mysql.connector.connect(
         host='localhost',   # change here
        user='root',
        password='admin@123',
        database='pythondb',
        connection_timeout=5,
        use_pure=True 
    )
    
if mycon.is_connected():
    print("Successfully Connected to Mysql database")
else :
     raise Exception("Unable to connect to database")

cursor = mycon.cursor()
