from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from bank_controller import create_account, get_all_accounts

DATABASE_URL = "sqlite:///bank.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(engine)

    # Example usage
    create_account(session, '123456789', 'John Doe', 1000.0)
    accounts = get_all_accounts(session)
    for account in accounts:
        print(f"Account Number: {account.account_number}, Owner: {account.owner_name}, Balance: {account.balance}")

    session.close()
