import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")