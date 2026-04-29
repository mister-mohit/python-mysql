import mysql.connector 
mycon = mysql.connector.connect(
         host='localhost',
        user='root',
        password='1008',
        database='sqlpractice',
        connection_timeout=5,
        use_pure=True 
    )
    
if mycon.is_connected():
    print("Successfully Connected to Mysql database")
else :
     raise Exception("Unable to connect to database")

cursor = mycon.cursor()
