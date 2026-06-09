import csv
import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_information"
)

cursor = db.cursor()

# CSV Read and Update MySQL
with open("student.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)

    query = """
            INSERT INTO records(ID, Name, Totle_fees, Branch)
            VALUES(%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            Name = VALUES(Name),
            Totle_fees = VALUES(Totle_fees),
            Branch = VALUES(Branch)
           """

    values = (
           
    row["ID"],
    row["Name"],
    row["Totle_fees"],
    row["Branch"]

        )

    cursor.execute(query, values)

# Save Changes
db.commit()

print("MySQL Updated Successfully")

cursor.close()
db.close()