import boto3

def upload(filename,bucket,output):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(filename, bucket, output)
    

    
