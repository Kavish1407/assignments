import boto3
client=boto3.client('dynamodb')
response = client.query(
    TableName='KavishGames',
    Select='SPECIFIC_ATTRIBUTES',
    AttributesToGet=[
        'Gname','Rating'
    ],
    Limit=123,
    ConsistentRead=True,
    KeyConditions={
        'GID': {
            'AttributeValueList': [
                {
                    'N': '2'
                }
            ],
            'ComparisonOperator': 'EQ'
        }
    }


)
print(response['Items'])
