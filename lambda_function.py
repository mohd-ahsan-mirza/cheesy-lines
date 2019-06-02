import boto3
import os
from boto3.dynamodb.conditions import Key
SES = boto3.client("ses")
DB_RESOURCE = boto3.resource('dynamodb')
DB_CLIENT = boto3.client('dynamodb')
CHARSET = os.environ['charset']
SOURCE_EMAIL = os.environ['source_email']
DESTINATION_EMAIL = os.environ['destination_email']
MAX_SENT = int(os.environ['max_sent'])
TABLE_NAME = os.environ['db_table']
TABLE = DB_RESOURCE.Table(TABLE_NAME)
FILTER_KEY = os.environ['filter_key']
def process():
    lines = get_lines()
    if len(lines) == 0:
        send_email("Add more cheesy lines","All out of cheesy lines!! Add more please to impress your SO",SOURCE_EMAIL,SOURCE_EMAIL)
    else:
        line = lines[0]
        print(line)
        send_email("Cheesy Line "+str(line['line_number']),line['line'],SOURCE_EMAIL,DESTINATION_EMAIL)
        updated_item = {'line_number': {"N":str(line['line_number'])},'sent':{"N":str(int(line['sent'])+1)},"line":{"S":line['line']}}
        DB_CLIENT.put_item(TableName=TABLE_NAME,Item=updated_item)
def get_lines():
    filtering_exp = Key(FILTER_KEY).lte(MAX_SENT)
    response = TABLE.scan(TableName=TABLE_NAME,FilterExpression=filtering_exp)
    result = response['Items']
    #print(result)
    return result
def send_email(subject,message,source_email,destination_email):
    response = SES.send_email(
        Destination={
            'BccAddresses': [
            ],
            'CcAddresses': [
                source_email,
            ],
            'ToAddresses': [
                destination_email,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': '<html><head></head><body>'+message+'</body></html>',
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': subject,
            },
        },
        Source=source_email
    )
    print(response)