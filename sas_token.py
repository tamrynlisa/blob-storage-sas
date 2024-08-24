from azure.storage.blob import BlobServiceClient, BlobClient, generate_blob_sas, BlobSasPermissions
import os
import datetime

def create_service_sas_blob(blob_client: BlobClient, account_key: str):
    # Create a SAS token that's valid for one day, as an example
    start_time = datetime.datetime.now(datetime.timezone.utc)
    expiry_time = start_time + datetime.timedelta(days=1)

    sas_token = generate_blob_sas(
        account_name=blob_client.account_name,
        container_name=blob_client.container_name,
        blob_name=blob_client.blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(write=True, create=True),
        expiry=expiry_time,
        start=start_time
    )

    return sas_token


# Initialize BlobServiceClient to access the storage account
account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')

blob_service_client = BlobServiceClient(account_url="https://stazureblobstorageex.blob.core.windows.net/", credential=account_key)
blob_client = blob_service_client.get_blob_client(container="files", blob="uploadedtextfile")

# Generate SAS token
sas_token = create_service_sas_blob(blob_client, account_key)

# Create the SAS URL
sas_url = f"{blob_client.url}?{sas_token}"

# Create a BlobClient object with SAS authorization
blob_client_sas = BlobClient.from_blob_url(blob_url=sas_url)

# Upload a file to the blob using the SAS token
file_path = "/home/tamryn/devopsTraining/blob-storage-sas/textfile.txt"
with open(file_path, "rb") as data:
    blob_client_sas.upload_blob(data, overwrite=True)

print(f"File '{file_path}' uploaded successfully to.")
print(f"sas_url: {sas_url} ")
