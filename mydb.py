#steps for starting new python project 
#install MySql
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python


import mysql.connector
database = mysql.connector.connect(host='localhost', user='root',passwd='password')

#prepare cursor object

cursorObject = database.cursor()

#create Database 

cursorObject.execute("CREATE DATABASE elderco")
print('Database created !!')
