import boto3
import csv
from csvWriter import writer
from s3Upload import upload
from classifierJobStart import startJob
import time
import datetime


            
def entityRecognizer(entity):
    temp={'NAME':'null','ORG':'null','MOBILE':'null'}
    for item in entity:
        if item['Type']=='PERSON':
            temp['NAME']=item['Text']
        elif item['Type']=='ORGANIZATION':
            temp['ORG']=item['Text']
        elif item['Type']=='OTHER':
            temp['MOBILE']=item['Text']
    return temp

def startAnalysis(filename,filenames):  
    client=boto3.client('comprehend')
    recordingsList=[]
    entityList=[]
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            recordingsList.append(row[0])
    sentimentResponse = client.batch_detect_sentiment(
        TextList=recordingsList,
        LanguageCode='en'
    )
    entityResponse = client.batch_detect_entities(
        TextList=recordingsList,
        LanguageCode='en'
    )
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    upload(filename,'pavanoutputbucket','InputData/{}.csv'.format(st))
    jobid=startJob(st)
    sentimentList=sentimentResponse['ResultList']
    entityList=entityResponse['ResultList']
    finalList=[]
    finalList.append([jobid])
    for idx,row in enumerate(recordingsList):
        temp=[]
        temp.append(sentimentList[idx]['Sentiment'])
        entity=entityRecognizer(entityList[idx]['Entities'])
        temp.append(entity['NAME'])
        temp.append(entity['ORG'])
        temp.append(entity['MOBILE'])
        temp.append(filenames[idx])
        finalList.append(temp)
    writer(finalList,'{}.csv'.format(st))
    
    
              
            
            
 

