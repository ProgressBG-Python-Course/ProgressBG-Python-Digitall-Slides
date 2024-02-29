from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class UserManager:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_user(self, name, age):
        session = self.Session()
        new_user = User(name=name, age=age)
        session.add(new_user)
        session.commit()
        session.close()

    def read_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    def update_user(self, user_id, name=None, age=None):
        session = self.Session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            if name:
                user.name = name
            if age:
                user.age = age
            session.commit()
        session.close()

    def delete_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

if __name__ == '__main__':
    # Create an instance of UserManager with a database URI
    db_uri = 'sqlite:///example.db'
    user_manager = UserManager(db_uri)

    # Create a new user
    user_manager.create_user(name='Ivan', age=30)

    # Read the user by ID
    user = user_manager.read_user(user_id=1)
    print(user.id, user.name, user.age)  # Output: 1 Ivan 30

    # Update the user's age
    user_manager.update_user(user_id=1, age=31)

    # Read the updated user
    user = user_manager.read_user(user_id=1)
    print(user.id, user.name, user.age)  # Output: 1 Ivan 31

    # Delete the user
    user_manager.delete_user(user_id=1)

    # Attempt to read the user (should return None)
    user = user_manager.read_user(user_id=1)
    print(user)  # Output: None
