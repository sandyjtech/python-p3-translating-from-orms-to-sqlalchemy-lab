from models import Base, Dog
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


def create_table():
    engine = create_engine('sqlite:///dogs.db')
    Base.metadata.create_all(engine)
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    
engine = create_table()