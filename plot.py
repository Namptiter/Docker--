import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="yourpass",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("USE mydatabase")

nhiet_do = []
do_am = []
X=[]
mycursor.execute("SELECT nhiet_do from data")

data = mycursor.fetchall()
for i in range(0,len(data)):
	X.append(i)
	nhiet_do.append(data[i][0])
nhiet_do = list(map(int, nhiet_do))

mycursor.execute("SELECT do_am from data")

data = mycursor.fetchall()
for i in range(0,len(data)):
	do_am.append(data[i][0])
do_am = list(map(int, do_am))

plt.subplot(2, 1, 1)
plt.plot(X,nhiet_do,color='orange')
plt.ylabel('Nhiet do °C')
plt.title("Bieu Do Nhiet Do")
plt.axis([-1,20,0,100])

plt.subplot(2, 1, 2)
plt.bar(X,do_am)
plt.ylabel('Do am %')
plt.title("Bieu Do Do am")
plt.axis([-1,20,0,100])
plt.show()
