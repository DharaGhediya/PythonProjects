# install MySQL driver
# remove comments and enjoy it!
import mysql.connector
"""
# Create Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dh@ra!6353?"
)
print(mydb)

# Creating a Database
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists....
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)
"""

# Try connecting to the database "mydatabase"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dh@ra!6353?",
  database="mydatabase"
)

mycursor = mydb.cursor()
# Creating a Table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), age VARCHAR(3))")

# Check if Table Exists
#mycursor.execute("SHOW TABLES")
#for y in mycursor:
#  print(y)

# Create primary key when creating the table:
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age VARCHAR(3))")
# Create primary key on an existing table (use the ALTER TABLE keyword):
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insert a record in the "customers" table
"""
sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
val = ("Dhara", 21)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
"""

# Insert Multiple Rows
"""
sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
val = [
  ('Peter', 20),
  ('Amy', 30),
  ('Hannah', 25),
  ('Michael', 22),
  ('Sandy', 23),
  ('Betty', 22),
  ('Richard', 25),
  ('Susan', 26),
  ('Vicky', 24),
  ('Ben', 25),
  ('William', 22),
  ('Chuck', 20),
  ('Viola', 26)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
"""

# Insert one row, and return the ID
"""
sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
val = ("Michelle", "28")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
"""

# Select all records from the "customers" table, and display the result
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
#myresult = mycursor.fetchone()
for i in myresult:
  print(i)

# Select only the name and age columns
mycursor.execute("SELECT name, age FROM customers")
myresult = mycursor.fetchall()
for j in myresult:
  print(j)

# filter records using where
sql = "SELECT * FROM customers WHERE age ='25'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for k in myresult:
  print(k)

# Update Table
sql = "UPDATE customers SET age = '21' WHERE age = '23'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete Record
sql = "DELETE FROM customers WHERE age = '22'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Delete a Table
#sql = "DROP TABLE customers"
#mycursor.execute(sql)