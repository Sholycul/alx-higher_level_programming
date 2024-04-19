#!/usr/bin/python3

"""
Script to delete all State objects with a name containing the letter 'a' from
the database hbtn_0e_6_usa.

Usage:
    python script.py <username> <password> <database_name>

Arguments:
    username: MySQL username.
    password: MySQL password.
    database_name: Name of the MySQL database.

This script connects to a MySQL server running on localhost at port 3306 and
deletes all State objects with a name containing the letter 'a' from the
specified database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database_name):
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

    # Query and delete State objects with a name containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)
    # Commit the changes
    session.commit()

    print(f"Deleted {len(states_with_a)} State objects.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:]

    delete_states_with_a(username, password, database_name)
