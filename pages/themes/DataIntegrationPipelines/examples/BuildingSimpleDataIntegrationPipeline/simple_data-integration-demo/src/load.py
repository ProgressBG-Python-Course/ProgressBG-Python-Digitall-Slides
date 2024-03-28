# main.py
from src.db.utils import init_db, get_session
from src.db.actions import insert_campaign, insert_crm_data

from src.extract import load_facebook_ads_data, load_google_analytics_data


engine = init_db()  # Initialize DB and create tables
session = get_session(engine)  # Get a session for DB operations

# Now pass the session object to the insert functions
insert_campaign(session, 1001, "Campaign Alpha")
insert_campaign(session, 1002, "Campaign Beta")
insert_campaign(session, 1003, "Campaign Gamma")

insert_crm_data(session, 2001, "John Doe", 3001, "2024-03-01", 150.00, 1001)
insert_crm_data(session, 2002, "Jane Smith", 3002, "2024-03-02", 250.00, 1002)
insert_crm_data(session, 2003, "Alex Johnson", 3003, "2024-03-03", 350.00, 1003)

# Close the session
session.close()
