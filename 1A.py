import mysql.connector

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_information ",
    use_pure=True
)

cursor = db.cursor()

search = input("Enter ID, Name or Branch: ")

query = """
SELECT * FROM records
WHERE id = %s OR Name = %s OR branch = %s
"""

cursor.execute(query, (search, search, search))

result = cursor.fetchall()

if result:
    print("\nRecords Found:\n")
    for row in result:
        print("ID         :", row[0])
        print("Name       :", row[1])
        print("Total Fees :", row[2])
        print("Branch     :", row[3])
        print("-" * 30)
else:
    print("No Record Found")

cursor.close()
db.close()