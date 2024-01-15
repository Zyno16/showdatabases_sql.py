import mysql.connector
try:
    conn = mysql.connector.connect(
        user ="userpython",
        host ="localhost",
        passwd ="123456"
        )
    cur=conn.cursor()
    cur.execute("SHOW DATABASES")
    for x in cur:
        print(x)
except mysql.connector.Error as e:
    print(e)

    
    
