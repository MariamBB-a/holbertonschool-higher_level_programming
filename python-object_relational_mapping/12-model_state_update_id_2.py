#!/usr/bin/python3
"""Changes the name of the State object with id = 2 to 'New Mexico'"""

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
        f"mysql+mysqldb://{user}:{passwd}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update its name if found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
