# Description
I built this application to email my girlfriend a new cheesy line everyday using AWS services

# Prerequisites
* Python => 3
* PIP3
* AWS-CLI
* boto3

# Setup

## AWS

### Dynamodb
Create a new cloudformation stack using template ```db-creation-cloudformation.json```

### Lambda
Create a new Lambda function using the code in ```lambda_function.py```

Configure all the environment variables present in the ```test_lambda_function_locally.py```

IAM policies you will need to attach
* AmazonDynamoDBFullAccess
* AmazonSESFullAccess

Name the function ```email_cheesy_line```

### CloudWatch
Create a new rule using the function name above and a schedule of your choice.

## Local

### AWS-CLI
Make sure you have added your keys for aws cli using ```aws-configure```

Install boto3 if you haven't previously ```pip3 install boto3```

### Seeding Data
Uncomment all seeded data if commented out in ```seed_data.py``` and run the file using ```python3```



 
