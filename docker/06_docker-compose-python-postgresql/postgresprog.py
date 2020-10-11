import psycopg2
import time
import os

postgres_location=os.environ['POSTGRES_LOCATION']

print("ip used by postgres:", postgres_location)

def connect():
    while True:
        try :
            return psycopg2.connect(user = "postgresuser",
                                    password = "postgrespassword",
                                    host = postgres_location,
                                    port = "5432",
                                    database = "postgresdb")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL. Retrying in 5 seconds...", error)
            time.sleep(5)

try:
    connection = connect()

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    cursor.execute("select * from information_schema.tables where table_name=%s", ("books",))

    if bool(cursor.rowcount):
        print("Table already exist")
    else:
        print("Table didn't exist. Creating table")
        cursor.execute(
            """CREATE TABLE books (
                 id              SERIAL PRIMARY KEY,
                 title           VARCHAR(100) NOT NULL,
                 primary_author  VARCHAR(100) NULL
               );""")
        cursor.execute("INSERT INTO books(title, primary_author) VALUES (%s,%s)", ("Robinson Crusoe", "Daniel Defoe"))
        connection.commit()

    i = 0

    while True:
        cursor.execute("SELECT * FROM books")
        books_records = cursor.fetchall()
        print("Records fetched. Iteration:", i)
        i += 1
        for record in books_records:
            print("id =", record[0], "title =", record[1], "author =", record[2])
        print()
        time.sleep(1)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
