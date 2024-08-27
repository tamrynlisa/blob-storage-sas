#!/bin/bash

SAS_TOKEN=$(az storage blob generate-sas \
    --account-name stazureblobstorageex \
    --container-name files \
    --name uploadedtextfile \
    --permissions acdrw \
    --expiry 2024-08-30T23:59:00Z \
    --auth-mode login \
    --as-user \
    --full-uri \
    --output tsv)

# Export the SAS token as an environment variable
echo "SAS_URL=${SAS_TOKEN}" >> $GITHUB_ENV