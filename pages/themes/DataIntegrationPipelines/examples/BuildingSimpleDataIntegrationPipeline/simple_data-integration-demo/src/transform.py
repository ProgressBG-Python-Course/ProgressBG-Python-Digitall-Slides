import pandas as pd
from datetime import datetime

def clean_facebook_ads_data(facebook_ads_df):
    """
    Cleans and prepares the Facebook Ads data.

    Parameters:
    - facebook_ads_df (pandas.DataFrame): DataFrame containing Facebook Ads data.

    Returns:
    - pandas.DataFrame: Cleaned and enriched DataFrame.
    """
    # Fill missing values with defaults
    facebook_ads_df.fillna({'impressions': 0, 'clicks': 0, 'spend': 0}, inplace=True)

    # Remove duplicates based on campaign_id and date
    facebook_ads_df.drop_duplicates(subset=['campaign_id', 'date'], keep='last', inplace=True)

    # Normalize date format
    facebook_ads_df['date'] = pd.to_datetime(facebook_ads_df['date']).dt.date

    # Calculate cost per click (CPC)
    facebook_ads_df['CPC'] = facebook_ads_df['spend'] / facebook_ads_df['clicks']
    facebook_ads_df['CPC'].fillna(0, inplace=True)  # Handle division by zero

    return facebook_ads_df

def clean_google_analytics_data(google_analytics_df):
    """
    Cleans and prepares the Google Analytics data.

    Parameters:
    - google_analytics_df (pandas.DataFrame): DataFrame containing Google Analytics data.

    Returns:
    - pandas.DataFrame: Cleaned and flattened DataFrame.
    """
    # Normalize date format
    google_analytics_df['date'] = pd.to_datetime(google_analytics_df['date']).dt.date

    # Flatten nested 'metrics' column
    metrics_df = pd.json_normalize(google_analytics_df['metrics'])
    google_analytics_df = pd.concat([google_analytics_df.drop('metrics', 1), metrics_df], axis=1)

    # Fill missing values
    google_analytics_df.fillna({'page_views': 0, 'conversions': 0, 'bounce_rate': '0%'}, inplace=True)

    # Convert bounce_rate to a decimal
    google_analytics_df['bounce_rate'] = google_analytics_df['bounce_rate'].str.rstrip('%').astype('float') / 100.0

    return google_analytics_df
