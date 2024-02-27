from model import BankAccount

def create_account(session, account_number, owner_name, balance):
    new_account = BankAccount(account_number=account_number, owner_name=owner_name, balance=balance)
    session.add(new_account)
    session.commit()

def get_all_accounts(session):
    return session.query(BankAccount).all()
