# actions.py
from datetime import datetime
from models import Campaign, CRMData

def insert_campaign(session, campaign_id, campaign_name):
    existing_campaign = session.query(Campaign).filter_by(campaign_id=campaign_id).first()
    if not existing_campaign:
        new_campaign = Campaign(campaign_id=campaign_id, campaign_name=campaign_name)
        session.add(new_campaign)
        session.commit()
        print(f"Added new campaign: {campaign_name}")
    else:
        print(f"Campaign already exists: {campaign_name}")

def insert_crm_data(session, customer_id, customer_name, order_id, order_date_str, order_amount, campaign_id):
    order_date = datetime.strptime(order_date_str, '%Y-%m-%d').date()
    new_crm_data = CRMData(
        customer_id=customer_id, customer_name=customer_name,
        order_id=order_id, order_date=order_date,
        order_amount=order_amount, campaign_id=campaign_id
    )
    session.add(new_crm_data)
    session.commit()
    print(f"Added new CRM record for {customer_name}")
