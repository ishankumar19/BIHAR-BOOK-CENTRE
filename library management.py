import mysql.connector as sql

mycon = sql.connect(host="localhost", user="root", passwd="ISHANsingh0612")
if mycon.is_connected():
    print("WELCOME TO BIHAR  BOOK CENTRE")

mycursor = mycon.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS project")
mycursor.execute("USE project")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS library_master (
        cardno VARCHAR(10) PRIMARY KEY,
        name_of_person VARCHAR(30),
        phone_no VARCHAR(15),
        address VARCHAR(100),
        DOB DATE
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        name VARCHAR(50),
        no VARCHAR(5) PRIMARY KEY,
        genre VARCHAR(30),
        author VARCHAR(50),
        language VARCHAR(30)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS lend (
        cardno VARCHAR(10),
        name_of_book VARCHAR(50),
        lend_date DATE,
        return_date DATE
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS order_book (
        order_no VARCHAR(10) PRIMARY KEY,
        book_name VARCHAR(50),
        delivery_date DATE,
        price INT
    )
""")

while True:
    print("""
    ----------------------------------
    ---------BIHAR BOOK CENTRE--------
    1. CREATE A NEW ACCOUNT
    2. SEE THE ACCOUNT INFO
    3. UPDATE CARD INFO
    4. DELETE THE ACCOUNT
    5. ADD A NEW BOOK
    6. SEE BOOKS
    7. UPDATE BOOK DETAILS
    8. DELETE BOOK
    9. LEND A BOOK
    10. RETURN THE BOOK
    11. DISPLAY LENDDING HISTORY
    12. ORDER A NEW BOOK
    13. UPDATE ORDER DETAILS
    14. DISPLAY ORDERING HISTORY
    15. EXIT
    ----------------------------------
    ----------------------------------
    """)

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("\n1. Go back\n2. Continue")
        cont = int(input("Enter your choice: "))
        if cont == 2:
            print("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER")
            cardno = input("Enter card no: ")
            name = input("Enter name (limit 30 characters): ")
            phone = input("Enter phone no: ")
            address = input("Enter the address (max 100 characters): ")
            dob = input("Enter the date of birth (yyyy-mm-dd): ")
            query = "INSERT INTO library_master VALUES (%s, %s, %s, %s, %s)"
            data = (cardno, name, phone, address, dob)
            mycursor.execute(query, data)
            mycon.commit()
            print("ACCOUNT IS SUCCESSFULLY CREATED!!!")

    elif ch == 2:
        cardno = input("Enter card no: ")
        query = "SELECT * FROM library_master WHERE cardno = %s"
        mycursor.execute(query, (cardno,))
        for i in mycursor:
            print(i)

    elif ch == 3:
        cardno = input("Enter card no to update: ")
        name = input("Enter new name: ")
        query = "UPDATE library_master SET name_of_person = %s WHERE cardno = %s"
        mycursor.execute(query, (name, cardno))
        mycon.commit()
        print("UPDATED SUCCESSFULLY")

    elif ch == 4:
        cardno = input("Enter card no to delete: ")
        query = "DELETE FROM library_master WHERE cardno = %s"
        mycursor.execute(query, (cardno,))
        mycon.commit()
        print("ACCOUNT DELETED")

    elif ch == 5:
        print("FILL ALL BOOK DETAILS")
        name = input("Enter book name: ")
        no = input("Enter book number: ")
        genre = input("Enter genre: ")
        author = input("Enter author name: ")
        language = input("Enter language: ")
        query = "INSERT INTO book VALUES (%s, %s, %s, %s, %s)"
        data = (name, no, genre, author, language)
        mycursor.execute(query, data)
        mycon.commit()
        print("BOOK ADDED SUCCESSFULLY")

    elif ch == 6:
        no = input("Enter book number: ")
        query = "SELECT * FROM book WHERE no = %s"
        mycursor.execute(query, (no,))
        for i in mycursor:
            print(i)

    elif ch == 7:
        no = input("Enter book number to update: ")
        author = input("Enter new author name: ")
        query = "UPDATE book SET author = %s WHERE no = %s"
        mycursor.execute(query, (author, no))
        mycon.commit()
        print("BOOK DETAILS UPDATED")

    elif ch == 8:
        no = input("Enter book number to delete: ")
        query = "DELETE FROM book WHERE no = %s"
        mycursor.execute(query, (no,))
        mycon.commit()
        print("BOOK DELETED")

    elif ch == 9:
        cardno = input("Enter card number: ")
        book = input("Enter book name: ")
        lend_date = input("Enter lending date (yyyy-mm-dd): ")
        return_date = input("Enter return date (yyyy-mm-dd): ")
        query = "INSERT INTO lend VALUES (%s, %s, %s, %s)"
        data = (cardno, book, lend_date, return_date)
        mycursor.execute(query, data)
        mycon.commit()
        print("BOOK LENT SUCCESSFULLY")

    elif ch == 10:
        cardno = input("Enter card number to delete lending record: ")
        query = "DELETE FROM lend WHERE cardno = %s"
        mycursor.execute(query, (cardno,))
        mycon.commit()
        print("LENDING RECORD DELETED")

    elif ch == 11:
        cardno = input("Enter card number to display history: ")
        query = "SELECT * FROM lend WHERE cardno = %s"
        mycursor.execute(query, (cardno,))
        for i in mycursor:
            print(i)

    elif ch == 12:
        order_no = input("Enter order number: ")
        book_name = input("Enter book name: ")
        delivery_date = input("Enter delivery date (yyyy-mm-dd): ")
        price = int(input("Enter price: "))
        query = "INSERT INTO order_book VALUES (%s, %s, %s, %s)"
        data = (order_no, book_name, delivery_date, price)
        mycursor.execute(query, data)
        mycon.commit()
        print("ORDER PLACED SUCCESSFULLY")

    elif ch == 13:
        order_no = input("Enter order number to update: ")
        delivery_date = input("Enter new delivery date (yyyy-mm-dd): ")
        query = "UPDATE order_book SET delivery_date = %s WHERE order_no = %s"
        mycursor.execute(query, (delivery_date, order_no))
        mycon.commit()
        print("ORDER UPDATED")

    elif ch == 14:
        order_no = input("Enter order number to display: ")
        query = "SELECT * FROM order_book WHERE order_no = %s"
        mycursor.execute(query, (order_no,))
        for i in mycursor:
            print(i)

    elif ch == 15:
        print("Have a nice day")
        break

    else:
        print("Invalid choice. Please try again.")
