import boto3
import os
SES = boto3.client("ses")
CHARSET = "UTF-8"
SOURCE_EMAIL = os.environ['source_email']
DESTINATION_EMAIL = os.environ['destination_email']
def send_email():
    response = SES.send_email(
        Destination={
            'BccAddresses': [
            ],
            'CcAddresses': [
                SOURCE_EMAIL,
            ],
            'ToAddresses': [
                DESTINATION_EMAIL,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': '<html><head></head><body>You’re So Hot You Would Make The Devil Sweat</body></html>',
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': 'You’re So Hot You Would Make The Devil Sweat',
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': 'Chessy line 1',
            },
        },
        Source=SOURCE_EMAIL
    )
    print(response)