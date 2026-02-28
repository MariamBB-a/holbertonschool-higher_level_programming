#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db_name),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
