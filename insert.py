import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="yourpass",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("USE mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS data (nhiet_do VARCHAR(255), do_am VARCHAR(255))")
# mycursor.execute("DELETE FROM data")

nhiet_do = []
do_am = []

print("Nhiet do: ")
for i in range (0,10):
	nhiet_do.append(input())

print("Nhap do am: ")
for i in range(0,10):
	do_am.append(input())

for row in range(0,10):
	sql = "INSERT INTO data (nhiet_do, do_am) VALUES (%s, %s)"
	val = (nhiet_do[row], do_am[row])
	mycursor.execute(sql, val)

mydb.commit()
