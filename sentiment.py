import boto3

client=boto3.client('comprehend')
response = client.batch_detect_sentiment(
    TextList=[
        "I dont like this at all.",
    ],
    LanguageCode='en'
)
print(response)