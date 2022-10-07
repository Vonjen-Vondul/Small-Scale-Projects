import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='myfirstdatabase'

)

cursor=mydb.cursor()
#cursor.execute('CREATE DATABASE IF NOT EXISTS myfirstdatabase')

#cursor.execute('CREATE TABLE students(name VARCHAR(150), address VARCHAR (255))')


#cursor.execute('ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

#this is adding many numerous codes to a database
'''sql='INSERT INTO students (namw, address) VALUES (%s,%s)'
val=[('Peter', 'Lowstreet 4'),
 ('Amy', 'Apple st 652'),
('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
('Sandy', 'Ocean blvd 2'),
 ('Betty', 'Green Grass 1'),
('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38'),
('William', 'Central st 954'),
 ('Chuck', 'Main Road 989'),
('Viola', 'Sideway 1633')
]
cursor.executemany(sql, val)

mydb.commit()

print(cursor.rowcount,'was inserted')'''

#this is used to insert new inf and retrive the last ID 

'''sql = "INSERT INTO students (namw, address) VALUES (%s, %s)"
val=val = ("Michelle", "Blue Village")
cursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", cursor.lastrowid)'''


#acesses all the values in a table

'''cursor.execute('SELECT * FROM students')

myresult=cursor.fetchall()
'''''''''''''''''' fetchone() #used to select one 
for i in myresult:
    print(i)'''

#this is used tp make specific selections 

'''sql="SELECT * FROM students WHERE address ='Park Lane 38'"

cursor.execute(sql)

myresult=cursor.fetchall()

for i in myresult:
    print(i)'''

#using LIKE and the wildcard %input% 

'''sql="SELECT * FROM students WHERE address LIKE '%way%'"

cursor.execute(sql)

myresult=cursor.fetchall()

for i in myresult:
    print(i)'''

#using query values 
'''sql = "SELECT * FROM students WHERE address = %s"
adr = ("Yellow Garden 2", )

cursor.execute(sql, adr)

myresult = cursor.fetchall()

for x in myresult:
 print(x);'''

#sorting by order of name 
'''sql = "SELECT * FROM students ORDER BY namw"
cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)'''

#ordering by descending order 
'''sql = "SELECT * FROM students ORDER BY namw DESC"
cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)'''

#this code is used for deleting information from a table 
'''sql = "DELETE FROM students WHERE address = 'Mountain 21'"

cursor.execute(sql)

mydb.commit()

print(cursor.rowcount, "record(s) deleted")'''

#this code is used to delete a table totally
'''sql = "DROP TABLE customers"

mycursor.execute(sql)'''
                #or 
'''sql = "DROP TABLE IF EXISTS customers"
cursor.execute(sql)
'''

#this code is updating the database
'''sql = "UPDATE students SET address = 'Canyon 123' WHERE address = 'Valley 345'"
cursor.execute(sql)

mydb.commit()'''

#this code picks the first 5 records
'''cursor.execute("SELECT * FROM students LIMIT 5")

myresult = cursor.fetchall()

for x in myresult:
    print(x)
'''

#this code picks 5 records but skips the number implied by the offset key 
'''cursor.execute("SELECT * FROM students LIMIT 5  OFFSET 3")

myresult = cursor.fetchall()

for x in myresult:
    print(x)
'''
'''cursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(150), fav VARCHAR (255))')'''
#
'''sql = "INSERT INTO users (id, name ,fav) VALUES (%s,%s, %s)"
val = [(1,'john', 154),
(2,'peter', 156),
(3,'amy', 155)]

cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount, "was inserted.")'''


'''sql = "SELECT \
users.name AS user, \
products.name AS favorite \
FROM users \
INNER JOIN products ON users.fav = products.id"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
    print(x)'''
