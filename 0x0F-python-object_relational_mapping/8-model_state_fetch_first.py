#!/usr/bin/python3

"""
Script to print the first State object from the database hbtn_0e_6_usa.

Usage:
    python script.py <username> <password> <database_name>

Arguments:
    username: MySQL username.
    password: MySQL password.
    database_name: Name of the MySQL database.

This script connects to a MySQL server running on
localhost at port 3306 and prints
the first State object from the specified database, based on states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_first_state(username, password, database_name):
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

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:]

    get_first_state(username, password, database_name)
