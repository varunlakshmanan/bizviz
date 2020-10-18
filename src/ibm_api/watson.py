import requests
import json
import ibm_watson_machine_learning
from ibm_botocore.client import Config
import ibm_boto3, os

API_KEY = os.environ['IBM_API_KEY']

def get_IAMP_token(API_KEY):
    authentication_url = "https://iam.cloud.ibm.com/identity/token"
    auth_data = {'grant_type':'urn:ibm:params:oauth:grant-type:apikey', 'apikey':API_KEY}

    IAM_response = requests.post(authentication_url, data=auth_data)
    IAM_response_data = IAM_response.json()
    IAM_access_token = IAM_response_data["access_token"]
    return IAM_access_token

def model(token):
    wml_credentials = {"url": "https://us-south.ml.cloud.ibm.com", "apikey": API_KEY}
    #client = ibm_watson_machine_learning.APIClient(wml_credentials)
    # print("Bob")
    # space_id = os.environ['IBM_space_id']
    # client.set.default_space(space_id)
    #
    # sofware_spec_uid = client.software_specifications.get_id_by_name("spss-modeler_18.2")
    #
    # metadata = {
    #     client.repository.ModelMetaNames.NAME: 'IBM',
    #     client.repository.ModelMetaNames.TYPE: 'fbprophet',
    #     client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: sofware_spec_uid
    # }
    #
    # published_model = client.repository.store_model(
    #     model=model,
    #     meta_props=metadata,)
    # model_uid = client.repository.get_model_uid(published_model)
    # models_details = client.repository.list_models()
    #
    # metadata = {
    #     client.deployments.ConfigurationMetaNames.NAME: "Virtual deployment of Stock forecasting model",
    #     client.deployments.ConfigurationMetaNames.VIRTUAL: {"export_format": "coreml"}
    # }
    #
    # created_deployment = client.deployments.create(model_uid, meta_props=metadata)

token = get_IAMP_token(API_KEY)
print(token)
model(token)