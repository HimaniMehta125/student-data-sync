import mysql.connector

try:

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="new_user",
        use_pure=True,
    )

    print("Database Connected")

    cursor = db.cursor()

   
    # sql = "update users SET age = %s where username = %s"

    # value = ("11", "Neel")

    # cursor.execute(sql, value)

    # db.commit()

    # print(cursor.rowcount, "row updated")

    cursor.execute("select * from users")

    result = cursor.fetchall()

    for row in result:
        print(row)

  

# username 
    user1 = input("What would you like to update?")

    if user1 == "username":

        user2 = input("which username you can update")

        if  user2 == "Himani":

            sql = "UPDATE users SET username = %s WHERE username = %s"

            value = ("Himani Patel", "Himani")

            cursor.execute(sql, value)

            db.commit()

            print("First row updated")

        if user2 == "Neel":

            sql = "UPDATE users SET username = %s WHERE passwd = %s"

            value = ("Rahul", "asdfghjkl")

            cursor.execute(sql, value)

            db.commit()

            print("Third row updated")
    else:
        print("envalid row")


# password



    if user1 == "password":

        user2 = input("which password you can update")

        if  user2 == "Himani":

           sql = "UPDATE users SET passwd = %s WHERE username = %s"

           value = ("himani123", "Himani")

           cursor.execute(sql, value)

           db.commit()

           print("First row password updated")

           

        if user2 == "Neel":
            sql = "UPDATE users SET passwd = %s WHERE username = %s"

            value = ("himani123", "Himani")

            cursor.execute(sql, value)

            db.commit()

            print("First row password updated")


            print("secon row updated")
    else:
        print("envalid row")





    

except Exception as e:
    print("Error :", e)