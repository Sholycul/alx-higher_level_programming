#!/usr/bin/python3

"""
Script to print the State object with the name passed as an argument from the
database hbtn_0e_6_usa.

Usage:
    python script.py <username> <password> <database_name> <state_name>

Arguments:
    username: MySQL username.
    password: MySQL password.
    database_name: Name of the MySQL database.
    state_name: Name of the state to search for.

This script connects to a MySQL server running on localhost at port 3306 and
retrieves and displays the State object with the specified name from the
specified database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_by_name(username, password, database_name, state_name):
    # Create MySQL connection string
    db_url = f"mysql://{username}:{password}@localhost:3306/{database_name}"

    # Create SQLAlchemy engine
    engine = create_engine(db_url)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session maker
    DBSession = sessionmaker(bind=engine)

    # Create a session
    session = DBSession()

    # Query State object by name
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1:]

    find_state_by_name(username, password, database_name, state_name)
