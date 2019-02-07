import boto3
import csv



def startJob(filename):
    client = boto3.client('comprehend', region_name='us-east-1')

    start_response = client.start_document_classification_job(
        JobName=filename,
        InputDataConfig={
            'S3Uri': 's3://pavanoutputbucket/InputData/{}.csv'.format(filename),
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 's3://pavanoutputbucket/OutputData'
        },
        DataAccessRoleArn='arn:aws:iam::645801241389:role/service-role/AmazonComprehendServiceRole-pavan',
        DocumentClassifierArn=
        'arn:aws:comprehend:us-east-1:645801241389:document-classifier/requestClassifier2'
    )

    return start_response['JobId']
    
