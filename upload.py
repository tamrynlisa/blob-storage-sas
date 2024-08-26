from azure.storage.blob import BlobClient
import os

# Create a BlobClient object with SAS authorization
sas_url = os.getenv('SAS_URL')
blob_client = BlobClient.from_blob_url(sas_url)

# Upload a file to the blob using the SAS token
file_path = "textfile.txt"
with open('path/to/your/file.txt', 'rb') as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"File '{file_path}' uploaded successfully.")