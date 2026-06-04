import mysql.connector

print("Step 1")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_information"
)

print("Step 2")

cursor = db.cursor()

search = input("Enter ID, Name or Branch: ")

print("Step 3:", search)

query = """
SELECT * FROM records
WHERE id = %s OR Name = %s OR branch = %s
"""

cursor.execute(query, (search, search, search))

print("Step 4")

result = cursor.fetchall()

print("Step 5")
print(result)

cursor.close()
db.close()