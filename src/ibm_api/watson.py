import requests
import json
import ibm_watson_machine_learning
from ibm_botocore.client import Config
import ibm_boto3, os

API_KEY = 'TckMpw8wWwh7c8-zOsN6ACB6HOqbISxuGRWuUPgjKxEz'

def get_IAMP_token(API_KEY):
    authentication_url = "https://iam.cloud.ibm.com/identity/token"
    auth_data = {'grant_type':'urn:ibm:params:oauth:grant-type:apikey', 'apikey':API_KEY}

    IAM_response = requests.post(authentication_url, data=auth_data)
    IAM_response_data = IAM_response.json()
    IAM_access_token = IAM_response_data["access_token"]
    return IAM_access_token

def model(token):
    url = "https://us-south.ml.cloud.ibm.com/ml/v4/models?version=2020-09-01"
    wml_credentials = {"url": "https://us-south.ml.cloud.ibm.com", "token":token,}
    client = ibm_watson_machine_learning.APIClient(wml_credentials)
    space_id = "f728ba4f-98b4-4e75-ae16-5db95d988e79"
    client.set.default_space(space_id)

    metadata = {
        client.repository.ModelMetaNames.NAME: 'IBM',
        client.repository.ModelMetaNames.TYPE: 'fbprophet',
    }

    published_model = client.repository.store_model(
        model=model,
        meta_props=metadata,)

token = get_IAMP_token(API_KEY)
print(token)
model(token)