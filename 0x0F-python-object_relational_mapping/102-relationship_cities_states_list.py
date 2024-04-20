#!/usr/bin/python3
"""Script to list all City objects from the database hbtn_0e_101_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    # Displaying the results
    for city in cities:
        state_name = city.state.name if city.state else "None"
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    session.close()
