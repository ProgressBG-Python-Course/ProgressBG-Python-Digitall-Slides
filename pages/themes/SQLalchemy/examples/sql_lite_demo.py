from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, insert

def create_user_table(engine, metadata):
    # Define user table
    user = Table('user', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('username', String(50), nullable=False),
                 Column('email', String(100), nullable=False)
                 )

    # Create tables
    metadata.create_all(engine)
    print("User table created successfully!")

def insert_data(engine, metadata):
    # Create a connection
    conn = engine.connect()

    # Define the data to be inserted
    data_to_insert = [
        {'username': 'user11', 'email': 'user1@example.com'},
        {'username': 'user12', 'email': 'user2@example.com'},
        {'username': 'user13', 'email': 'user3@example.com'}
    ]

    try:
        # Get the table object
        user_table = Table('user', metadata, autoload=True)

        # Create an Insert object
        insert_stmt = insert(user_table).values(data_to_insert)

        # Execute the Insert object
        conn.execute(insert_stmt)

        # Commit the transaction
        conn.commit()

        print("Data inserted successfully.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if conn:
            conn.close()

def select_all_rows(engine, metadata):
    # Select all rows from the user table
    # Create a connection
    conn = engine.connect()

    try:
        # Get the table object
        user_table = Table('user', metadata, autoload=True)

        query = select(user_table)
        result = conn.execute(query)

        # Iterate over the result set
        for row in result:
            print(row)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__=='__main__':
    # Define the database connection string
    engine = create_engine('sqlite:///users.db', echo=True)

    # Define metadata
    metadata = MetaData()

    # Create user table if not exists
    create_user_table(engine, metadata)

    # Insert data
    insert_data(engine, metadata)

    # Select all rows
    select_all_rows(engine, metadata)
