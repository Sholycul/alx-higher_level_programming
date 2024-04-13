#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    List all states with a name starting with 'N' (upper N)
    from the database hbtn_0e_0_usa.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # executing the cursor to retrieve states sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetching all the results
    states = cursor.fetchall()

    # display/print them out
    for state in states:
        if state[1][0] == 'N':
            print(state)

    # closing the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
