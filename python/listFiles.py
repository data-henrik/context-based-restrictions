# Connect to IBM Cloud Object Storage and first retrieve all
# buckets, then connect to the "cbrbucket" and list the
# available items (files / objects).

# Sample file for tests with IBM Cloud context-based restrictions,
# most of the code is taken from
# https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-python#python-examples

# Adapted by Henrik Loeser, hloeser@de.ibm.com

import ibm_boto3
from ibm_botocore.client import Config, ClientError
import os
# for loading .env
from dotenv import load_dotenv

# load environment
load_dotenv()
# Constants for IBM COS values
COS_ENDPOINT = os.getenv('COS_ENDPOINT',"https://s3.eu-de.cloud-object-storage.appdomain.cloud")
COS_API_KEY_ID = os.getenv('COS_API_KEY_ID')
COS_INSTANCE_CRN = os.getenv('COS_INSTANCE_CRN')

# Create resource (configuration to access COS instance)
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

# list the available buckets
def get_buckets():
    print("Retrieving list of buckets")
    try:
        buckets = cos.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}".format(bucket.name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

# list the files in the bucket
def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        files = cos.Bucket(bucket_name).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))

# invoke the above two routines
get_buckets()
get_bucket_contents('cbrbucket')