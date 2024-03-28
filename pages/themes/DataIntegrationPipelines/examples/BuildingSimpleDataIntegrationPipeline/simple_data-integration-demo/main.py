from src.extract import load_facebook_ads_data, load_google_analytics_data
from src.transform import clean_facebook_ads_data, clean_google_analytics_data

# Paths to the raw data files
facebook_ads_csv_path = 'data/facebook_ads_data.csv'
google_analytics_json_path = 'data/google_analytics_data.json'

# Extract the data
facebook_ads_df = load_facebook_ads_data(facebook_ads_csv_path)
google_analytics_df = load_google_analytics_data(google_analytics_json_path)

# Transform the data
facebook_ads_df = clean_facebook_ads_data(facebook_ads_df)
google_analytics_df = clean_google_analytics_data(google_analytics_df)

print(facebook_ads_df)
print(google_analytics_df)

