import sqlite3
conn = sqlite3.connect("Library.db")
print("Database connected")


# Question1
conn.execute('''CREATE TABLE BOOKS(BOOK_ID INT PRIMARY KEY NOT NULL,TITLE_ID INT NOT NULL,LOCATION CHAR(20),GENRE CHAR(30));''')
print("Table Books created")

conn.execute('''CREATE TABLE Titles(TITLE_ID INT PRIMARY KEY NOT NULL,TITLE CHAR(10) NOT NULL,ISBN INT NOT NULL,PUBLISHER_ID INT NOT NULL,PUBLISHING_YEAR INT NOT NULL);''')
print("Table Titles created")

conn.execute('''CREATE TABLE Publishers(PUBLISHER_ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,STREET_ADDRESS CHAR(50) NOT NULL,SUITE_NUMBER INT NOT NULL,ZIP_CODE_ID INT NOT NULL); ''')
print("Table PUBLISHERS CREATED")

conn.execute('''CREATE TABLE ZIP_CODES(ZIP_CODE_ID INT PRIMARY KEY NOT NULL,CITY CHAR(10) NOT NULL,STATE CHAR(10) NOT NULL,ZIPCODE INT NOT NULL);''')
print("Table Zipcode created")

conn.execute('''CREATE TABLE Author_Titles(AUTHOR_TITLE_ID INT PRIMARY KEY NOT NULL,AUTHOR_ID INT NOT NULL,TITLE_ID INT NOT NULL);''')
print("table Author Titles Created")

conn.execute('''CREATE TABLE Authors(AUTHOR_ID INT PRIMARY KEY NOT NULL,FIRST_NAME CHAR(15) NOT NULL,MIDDLE_NAME CHAR(15) NOT NULL,LAST_NAME CHAR(15) NOT NULL);''')
print("table Authors created")



# QUESTION2

conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(3,121,'CHANDIGARH','THIS BOOK IS')")
print("data inserted")

conn.execute("INSERT INTO Titles(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLICATION_YEAR)VALUES(1,"THIS BOOK IS",'CHANDIGARH','THIS BOOK IS')")
print("data inserted")

conn.execute("INSERT INTO Publishers(PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID)VALUES(1,'fdfdf','CHANDIGARH',4,6)")
print("data inserted")

conn.execute("INSERT INTO TABLE ZIP_CODES(ZIP_CODE_ID,NAME,CITY,STATE,ZIPCODE)VALUES(1,'fdfdf','CHANDIGARH','fdsdfsd',6)")
print("data inserted")

conn.execute("INSERT INTO TABLE Author_Titles(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID)VALUES(1,2,'CHANDIGARH',6)")
print("data inserted")

conn.execute("INSERT INTO Authors(AUTHOR_ID,NAME,FIRST_NAME,MIDDLE_NAME,LAST_NAME)VALUES(1,'fdfdf','CHANDIGARH','fdsdfsd','djsjn')")



# QUESTION3

cursor = conn.execute("SELECT AUTHOR_ID,NAME,FIRST_NAME,MIDDLE_NAME,LAST_NAME from Authors")
print(cursor)
for row in cursor:
    print("AUTHOR_ID =", row[0])
    print("NAME =", row[1])
    print("FIRST_NAME =", row[2])
    print("MIDDLE_NAME =", row[3])
    print("LAST_NAME =", row[4], "\n")
print("operation done")


cursor = conn.execute("UPDATE  set FIRST_NAME = 'RAJA' where AUTHOR_ID = 1")

cursor = conn.execute("SELECT AUTHOR_ID,NAME,FIRST_NAME,MIDDLE_NAME,LAST_NAME from Authors")
print(cursor)
for row in cursor:
    print("AUTHOR_ID =", row[0])
    print("NAME =", row[1])
    print("FIRST_NAME =", row[2])
    print("MIDDLE_NAME =", row[3])
    print("LAST_NAME =", row[4], "\n")
print("operation done")