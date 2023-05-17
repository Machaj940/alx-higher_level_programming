#!/usr/bin/python3
'''Write a script that update the name of a State object Arizona to new mexico
'''


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})

    session.commit()

    session.close()
