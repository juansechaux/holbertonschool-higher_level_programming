#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    """Get arguments  from command-line"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    citys_and_states = session.query(City, State).join(State).all()

    for city, state in citys_and_states:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
