import boto3
import pprint
client=boto3.client('dynamodb')
table = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'GID',
            'AttributeType': 'N'
        }
    ],
    TableName='KavishGames',
    KeySchema=[
        {
            'AttributeName': 'GID',
            'KeyType': 'HASH'
        }
    ],
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
    },
)
pprint.pprint(table)


