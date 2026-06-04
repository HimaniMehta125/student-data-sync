import hashlib
import mysql.connector
import subprocess
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="new_user",
    use_pure=True
)

cursor = db.cursor()

# Signup

username = input("Enter your username : ")

password = input("Enter your password : ")

hash_password = hashlib.sha256(
    password.encode()
).hexdigest()

sql = """

INSERT INTO users(username,passwd)

VALUES(%s,%s)

"""

value = (username, hash_password)

cursor.execute(sql, value)

db.commit()

print("Signup Successful")

# Login Page

login_username = input("Enter your username : ")

login_passwd = input("Enter your password : ")

if login_username == username and login_passwd == password:

    print("Login Successfully")

    subprocess.run([sys.executable, "expens.py"])

else:

    print("Invalid Username or Password")

db.close()