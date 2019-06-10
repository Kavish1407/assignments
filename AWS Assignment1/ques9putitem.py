import boto3
client=boto3.client('dynamodb')
response = client.put_item(
    TableName='KavishGames',
    Item={
        'GID': {
            'N': '1'
    },
        'Gname': {
            'S': 'Cricket2007'
        },
        'Publisher': {
            'S': 'EA Sports'
        },
        'Rating': {
            'N': '9'
        },
        'Release_date': {
            'S': '5th May 2019'
        },
        'geners': {
            'SS':['Sports','Action']
        }

    }
)
response = client.put_item(
    TableName='KavishGames',
    Item={
            'GID': {
                'N': '2'
            },
            'Gname': {
                'S': 'PlayerUnknownBattleGround'
            },
            'Publisher': {
                'S': 'Gamers'
            },
            'Rating': {
                'N': '10'
            },
            'Release_date': {
                'S': '3th May 2017'
            },
            'geners': {
                'SS': ['Sports', 'Action','Adventure']
            }

        }
)

