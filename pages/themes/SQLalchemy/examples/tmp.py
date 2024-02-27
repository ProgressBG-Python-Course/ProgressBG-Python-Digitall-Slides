from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Create an engine
engine = create_engine('sqlite:///mydatabase.db')

# Declare a base using declarative_base
Base = declarative_base()

# Define the User class inheriting from Base
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

data = [
    {"name": "Ivan", "age": 30},
    {"name": "Mariya", "age": 25},
    {"name": "Petar", "age": 35}
]

# Iterate over the list of dictionaries and add each record to the session
for entry in data:
    new_user = User(name=entry['name'], age=entry['age'])
    session.add(new_user)

# Commit the session to persist the changes
session.commit()