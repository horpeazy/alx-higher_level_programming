#!/usr/bin/python3
""" This modules uses sqlachemy to query the database """

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    import sys

    # create an engine
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
