import json
import boto3
from boto3.dynamodb.conditions import Key,Attr

def Feedback(dynamodb):
      try:
          Feedback = dynamodb.create_table(TableName='Feedback',
                                KeySchema=[
                                    {
                                        'AttributeName': 'date',
                                        'KeyType': 'HASH'  # Partition key
                                    },
                                    {
                                        'AttributeName': 'time',
                                        'KeyType': 'RANGE'  # Sort key
                                    }
                                ], 
                                AttributeDefinitions=[
                                    {
                                        'AttributeName': 'date',
                                        'AttributeType': 'S'
                                    },
                                    {
                                        'AttributeName': 'time',
                                        'AttributeType': 'S'
                                    },
                                ],
                                ProvisionedThroughput={
                                    'ReadCapacityUnits': 2, #讀取容量
                                    'WriteCapacityUnits': 2 #寫入容量
                                }
                               )
          print("Table creat!")
          
      except Exception as e:
            print("Error creat table:")
            print(e)
        