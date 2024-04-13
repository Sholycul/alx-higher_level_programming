#!/usr/bin/python3

"""
This script fetches all cities from the 'hbtn_0e_4_usa' database.
It requires three parameters: MySQL username,
MySQL password, and database name.
The script utilizes the `MySQLdb` module for database interaction.
Connection is made to a MySQL server running on `localhost` at port `3306`.
Results are sorted in ascending order based on the `cities.id` column.
Only one call to `execute()` function is allowed.
The script is designed not to be executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the cursor to retrieve cities sorted by id
    city_query = """SELECT cities.id, cities.name, states.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query)

    # Fetching all the results
    cities = cursor.fetchall()

    # Displaying the results
    for city in cities:
        print(city)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
