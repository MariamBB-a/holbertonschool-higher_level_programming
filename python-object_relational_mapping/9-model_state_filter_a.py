#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all states containing 'a', ordered by id
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
