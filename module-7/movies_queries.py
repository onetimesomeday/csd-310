import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio")
    result = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for x in result:
        print("Studio ID: {}\n Studio Name: {}\n".format(x[0], x[1]))
    
    cursor.execute("SELECT * FROM genre")
    result = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")
    for x in result:
        print("Genre ID: {}\n Genre Name: {}\n".format(x[0],x[1]))
    
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    result = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for x in result:
        print("Film Name: {}\nRuntime: {}\n".format(x[0],x[1]))
    
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    result = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for x in result:
        print("Film Name: {}\nDirector: {}\n".format(x[0],x[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()


