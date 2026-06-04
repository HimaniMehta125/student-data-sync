import mysql.connector

db = mysql.connector.connect(

        host = "localhost",
        user = "root",
        password = "12345",
        database = "student_information",
        use_pure=True
)

cursor = db.cursor()

cursor.execute("select * from records")

result = cursor.fetchall()

for row in result:
        print(row)



print("After shorting")



#  id sorting


# n = len(result)

  
# for i in range(n):
#     for j in range(n - 1 - i):

#         if result[j][0] > result[j + 1][0]:   

#             temp = result[j]
#             result[j] = result[j + 1]
#             result[j + 1] = temp

# print("After Sorting:")

# for row in result:
#     print(row)




# fees sorting   


# n = len(result)

# for i in range(n):
#     for j in range(n - 1 - i):

#         if result[j][2] > result[j + 1][2]:   # Name compare

#             temp = result[j]
#             result[j] = result[j + 1]
#             result[j + 1] = temp

# for row in result:
#     print(row)


# Name sorting


# n = len(result)

# for i in range(n):
#     for j in range(n - 1 - i):

#         if result[j][1] > result[j + 1][1]:   # Name compare

#             temp = result[j]
#             result[j] = result[j + 1]
#             result[j + 1] = temp

# for row in result:
#     print(row)