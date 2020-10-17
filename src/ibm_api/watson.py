import requests
import os
import json

os.environ['IBM_API_KEY'] = 'TckMpw8wWwh7c8-zOsN6ACB6HOqbISxuGRWuUPgjKxEz'
API_KEY = os.environ['IBM_API_KEY']

def get_IAMP_token(API_KEY):
    authentication_url = "https://iam.cloud.ibm.com/identity/token"
    auth_data = {'grant_type':'urn:ibm:params:oauth:grant-type:apikey', 'apikey':API_KEY}

    IAM_response = requests.post(authentication_url, data=auth_data)
    IAM_response_data = IAM_response.json()
    IAM_access_token = IAM_response_data["access_token"]
    return IAM_access_token

