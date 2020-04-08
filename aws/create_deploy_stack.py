import boto3
from botocore.exceptions import ClientError

name = "millermaskproject"
client = boto3.client('cloudformation')
try:
    data = client.describe_stack(StackName = name)
except ClientError:
    client.delete_stack(StackName=name)
    client.create_stack(StackName=name, Capabilities=['CAPABILITY_NAMED_IAM'])

if data['Stacks'][0][['StackStatus'] == 'ROLLBACK_COMPLETE':
    client.create_stack(StackName=name, Capabilities=['CAPABILITY_NAMED_IAM'])
else:
    client.update_stack(StackName=name, Capabilities=['CAPABILITY_NAMED_IAM'])

