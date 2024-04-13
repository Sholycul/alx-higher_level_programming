#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(argv) != 5:
        print(f"Usage: {argv[0]} <username> <password> <database> <state>")
        exit(1)

    # Establish a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the cursor to retrieve cities of the specified state sorted by id
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (argv[4],))

    # Fetch all the results
    cities = cursor.fetchall()

    # Extract city names and join them with commas
    city_names = ', '.join(str(city[0]) for city in cities)

    # Display the results
    print(city_names)

    # Close the cursor and database connection
    cursor.close()
    db.close()
