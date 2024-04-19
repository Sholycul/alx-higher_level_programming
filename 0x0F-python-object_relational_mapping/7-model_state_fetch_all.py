#!/usr/bin/env python3

"""
Script to list all State objects from the database hbtn_0e_6_usa.

Usage:
    python script.py <username> <password> <database_name>

Arguments:
    username: MySQL username.
    password: MySQL password.
    database_name: Name of the MySQL database.

This script connects to a MySQL server running on 
localhost at port 3306 and retrieves
and displays all State objects from the specified database,
sorted in ascending order by states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database_name):
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

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:]

    list_states(username, password, database_name)
