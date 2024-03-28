import requests
import base64


def upload_file(file_path, api_endpoint, token):
    """ Upload file to github api

    API docs:https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents

    Args:
        file_path (_type_): _description_
        api_endpoint (_type_): _description_
        token (_type_): _description_
    """
    with open(file_path, 'rb') as f:
        data = f.read()

    encoded_data = base64.b64encode(data).decode('utf-8')
    payload = {
        "message": "Upload file via API",
        "content": encoded_data
    }
    headers = {
        "Authorization": f"Bearer {token}",     # Use Bearer authentication
        "Accept": "application/vnd.github+json" ,
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.put(api_endpoint, headers=headers, json=payload)

    if response.status_code == 201:
        print("File uploaded successfully!")
    else:
        print("Upload failed:", response.text)

# --------  Configuration --------
file_to_upload = "./test.csv"
api_endpoint = "https://api.github.com/repos/ProgressBG-Python-Course/Shared/contents/test.csv"
token = "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"

# -------- Usage --------
upload_file(file_to_upload, api_endpoint, token)
