from sqlalchemy import create_engine, MetaData

# Create an engine to connect to the database
engine = create_engine('sqlite:///example.db')

# Reflect the database schema
metadata = MetaData()
metadata.reflect(bind=engine)

# Print all tables in db
for table in metadata.tables.values():
    print(table.name)

# Retrieve a table
users_table = metadata.tables['users']

# Get table columns
print(users_table.columns)