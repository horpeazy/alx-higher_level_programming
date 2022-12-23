#!/usr/bin/python3
""" This modules uses sqlachemy to query the database """

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    # create an engine
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
