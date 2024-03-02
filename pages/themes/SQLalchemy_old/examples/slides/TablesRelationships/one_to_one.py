from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Create engine
engine = create_engine('sqlite:///store.db:', echo=False)

# Create base class
Base = declarative_base()

# Define User class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # One-to-one relationship with Profile
    profile = relationship("Profile", uselist=False, back_populates="user")

# Define Profile class
class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)

    # One-to-one relationship with User
    user = relationship("User", back_populates="profile")

# Create tables in database
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Test relationship
user1 = User(name='Maria')
profile1 = Profile(bio='Maria is a software engineer', user=user1)

session.add_all([user1, profile1])
session.commit()

# Query example
user = session.query(User).first()
print("User:", user.name)
print("Profile:", user.profile.bio)

# Close session
session.close()
