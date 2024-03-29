#!/usr/bin/python3
"""
script that lists all State objects in asc order from the database hbtn_0e_6_usa
via SQLAlchemy
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine1 = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine1)
    session = Session()
    for instance in session.query(State).all():
        print("{}: {}".format(instance.id, instance.name))
    session.close()
