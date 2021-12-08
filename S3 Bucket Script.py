#!/usr/bin/env python3
import boto3
# uses credentials from default profile of AWS CLI
s3 = boto3.client('s3')
session = boto3.Session(profile_name='default')
client = session.client('s3')
bucket_name = "demo-bucket"
response = client.create_bucket(Bucket=bucket_name)
print("Amazon S3 bucket has been created")
