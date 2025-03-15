import mysql.connector

# Connect to the database
"""mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    
)

print(mydb)"""


#create a database
"""mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")"""


#Check if Database Exists
"""mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",

)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
"""

#Create primary key when creating the table
"""mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"

)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

"""

