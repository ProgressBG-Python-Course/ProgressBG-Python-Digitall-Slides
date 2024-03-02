from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Create engine
engine = create_engine('sqlite:///store.db', echo=False)

# Create base class
Base = declarative_base()

# Define Country class (Parent)
class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Establishing one-to-many relationship with User class
    users = relationship("User", back_populates="country")

# Define User class (Child)
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.id'))  # Foreign key linking to Country id

    # Establishing many-to-one relationship with Country class
    country = relationship("Country", back_populates="users")

# Create tables in database
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Test relationship
# Create some Country and User instances
country1 = Country(name='Bulgaria')
country2 = Country(name='Canada')

user1 = User(name='Ivan', country=country1)
user2 = User(name='Petar', country=country1)
user3 = User(name='Maria', country=country2)

# Add instances to session and commit changes to database
session.add_all([country1, country2, user1, user2, user3])
session.commit()

# Query example
# Query for all users in a country
country = session.query(Country).filter_by(name='Bulgaria').first()
print(f'Users in Bulgaria: ')
for user in country.users:
    print(user.name)

# Query for a user country:
user = session.query(User).filter_by(name="Maria").first()
print(f'{user.name} live in {user.country.name}')

# Close session
session.close()