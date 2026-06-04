import csv
import mysql.connector

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_information"
)

cursor = db.cursor()

print("Database Connected Successfully")

# User Input
id = int(input("Enter ID: "))
name = input("Enter Name: ")
branch = input("Enter Branch: ")
fees = int(input("Enter Total Fees: "))

# Insert into MySQL
query = """
INSERT INTO records(id, Name, Totle_fees, branch)
VALUES (%s, %s, %s, %s)
"""

values = (id, name, fees, branch)

cursor.execute(query, values)

db.commit()

print("Data Stored in MySQL Successfully")

# Export latest database data to CSV
cursor.execute("SELECT * FROM records")

rows = cursor.fetchall()

with open("student.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Totle_fees", "Branch"])

    writer.writerows(rows)

print("CSV Updated Successfully")


# CSV → MySQL Sync

with open("student.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute(
            """
            UPDATE records
            SET Name=%s,
                Totle_fees=%s,
                branch=%s
            WHERE id=%s
            """,
            (
                row["Name"],
                row["Totle_fees"],
                row["Branch"],
                row["ID"]
            )
        )

db.commit()

print("MySQL Updated From CSV")

db.close()