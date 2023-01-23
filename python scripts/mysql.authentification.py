import mysql.connector

accounts_database=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='accounts'
)
the_cursor = accounts_database.cursor()

#the_cursor.execute('CREATE DATABASE IF NOT EXISTS Accounts')

#the_cursor.execute('CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(20), password VARCHAR (8))')

for x in range(1):
    username =input('create new username: ')
    pass_word =input('create new password: ')
    sql='INSERT INTO users (user_name, password) VALUES (%s,%s)'
    val=(username, pass_word)
    
    try:
        the_cursor.execute(sql,val)
        accounts_database.commit()
        print(the_cursor.rowcount,'user saved successfully')
    
    except mysql.connector.Error as error:
        print('format error')



UserName =input('enter your username: ')

sql = "SELECT * FROM users WHERE user_name = %s"
Val = (UserName,)


the_cursor.execute(sql,Val)
myresult = the_cursor.fetchone()
print(the_cursor.rowcount,'user authenticated successfully')
