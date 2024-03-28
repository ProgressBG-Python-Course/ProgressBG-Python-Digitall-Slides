import pandas as pd
import json

def load_facebook_ads_data(csv_file_path):
    """Loads Facebook Ads data from a CSV file.

    Parameters:
    csv_file_path (str): The path to the CSV file containing Facebook Ads data.

    Returns:
    pandas.DataFrame: A DataFrame containing the loaded data.
    """
    return pd.read_csv(csv_file_path)

def load_google_analytics_data(json_file_path):
    """Loads Google Analytics data from a JSON file.

    Parameters:
    json_file_path (str): The path to the JSON file containing Google Analytics data.

    Returns:
    pandas.DataFrame: A DataFrame containing the loaded data.
    """
    with open(json_file_path) as f:
        data = json.load(f)

    if data:
        df = pd.json_normalize(data)
    return df