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
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",

)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

