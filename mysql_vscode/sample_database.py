import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    
    user='fahis_usr',
    password='Fhs@12345',
    database="groceries" 
    
)


cursor = mydb.cursor() 

cursor.execute("create table  sample_tbl3s(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),age INT)")
query = "INSERT INTO sample_tbl3s(name, age) VALUES (%s, %s)"
values=[("john",30),
        ("alice",25),
        ("eva",28),
        ("bob",35),
        ("bama",30),
        ("frank",45),
        ("hendry",29),
        ("ivy",33),
        ("grace",27),
        ("diana",31)]

   

cursor.executemany(query, values)
mydb.commit()

cursor.execute("SELECT * FROM sample_tbl3s")
result = cursor.fetchall()
for row in result:
    print(row)
    
cursor.close()
mydb.close()