# # import mysql.connector

# # print("Program Started")

# # try:
# #     db = mysql.connector.connect(
# #         host="localhost",
# #         user="root",
# #         password="12345",
# #         port=3306,
# #         auth_plugin="mysql_native_password",
# #         use_pure=True
# #     )

# #     print("After Connection Line")

# #     if db.is_connected():
# #         print("MySQL Connected Successfully")

# #     else:
# #         print("Not Connected")

# # except Exception as err:
# #     print("Error :", err)

# # print("Program Ended")


# import mysql.connector


# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "12345",
#     port = 3306,
#     database = "new_user",
#     use_pure=True

# )

# print("connection is done")
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="new_user",
        use_pure=True

    )

    if db.is_connected():
        print("Database Connected Successfully")

    else:
        print("Database Not Connected")

except mysql.connector.Error as err:
    print("Error :", err)



cursor = db.cursor()

sql = "delete from users where  username = %s"

value = ("Himani",)
cursor.execute(sql,value)

db.commit()
print("Row Deleted Successfully")