import boto3


# Instantiate Boto3 SDK:
client = boto3.client('comprehend', region_name='us-east-1')

start_response = client.start_document_classification_job(
    InputDataConfig={
        'S3Uri': 's3://pavanoutputbucket/InputData/inputData.csv',
        'InputFormat': 'ONE_DOC_PER_LINE'
    },
    OutputDataConfig={
        'S3Uri': 's3://pavanoutputbucket/OutputData'
    },
    DataAccessRoleArn='arn:aws:iam::645801241389:role/service-role/AmazonComprehendServiceRole-pavan',
    DocumentClassifierArn=
    'arn:aws:comprehend:us-east-1:645801241389:document-classifier/requestType'
)

print("Start response: %s\n", start_response)

# Check the status of the job
describe_response = client.describe_document_classification_job(JobId=start_response['JobId'])
print("Describe response: %s\n", describe_response)
