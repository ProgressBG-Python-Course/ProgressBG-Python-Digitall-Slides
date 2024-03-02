from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Create engine
engine = create_engine('sqlite:///store.db', echo=False)

# Create base class
Base = declarative_base()

# Define association table for many-to-many relationship
user_group_association = Table('user_group_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)

# Define User class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define many-to-many relationship with Group
    groups = relationship("Group", secondary=user_group_association, back_populates="users")

# Define Group class
class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define many-to-many relationship with User
    users = relationship("User", secondary=user_group_association, back_populates="groups")

# Create tables in database
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Test relationship
user1 = User(name='Ivan')
user2 = User(name='Maria')
group1 = Group(name='Developers')
group2 = Group(name='Designers')

user1.groups.append(group1)
user1.groups.append(group2)
user2.groups.append(group1)

session.add_all([user1, user2, group1, group2])
session.commit()

# Query example
group = session.query(Group).filter_by(name='Developers').first()
print("Group:", group.name)
print("Users in", group.name, "group:")
for user in group.users:
    print(user.name)

# Close session
session.close()
