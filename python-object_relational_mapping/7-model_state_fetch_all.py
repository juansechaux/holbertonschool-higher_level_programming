#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Get arguments  from command-line"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    for id_state, name_state in session.query(State.id, State.name):
        print('{}: {}'.format(id_state, name_state))
