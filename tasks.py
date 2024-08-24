from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions
from datetime import datetime, timedelta
import os
import sys
from invoke import task

@task
def hello(ctx):
    print("Hello, world!")
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    print({connection_string})

    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
    print({account_key})
