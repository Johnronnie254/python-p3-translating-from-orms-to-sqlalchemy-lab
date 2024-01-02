#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f"({self.id}) {self.name} {self.breed}" if self.id else f"{self.name} {self.breed}"

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

Osama_dog = Dog("Nyadala", "Nyaugenya")
Sadam_dog = Dog("Onyango", "Jamigori")
Chiwawa_dog = Dog("KRG", "The Donkey")
session.bulk_save_objects([Osama_dog, Sadam_dog, Chiwawa_dog])
session.commit()

results = session.query(Dog).all()

