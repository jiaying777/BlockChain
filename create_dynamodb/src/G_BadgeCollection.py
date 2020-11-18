import json
import boto3
from boto3.dynamodb.conditions import Key,Attr


def G_BadgeCollection(dynamodb):
		try:
			G_BadgeCollection = dynamodb.create_table(TableName='G_BadgeCollection',
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

def G_BadgeCollection_GlobalSecondary_applicantIndex(dynamodb):
		try:
		    response = dynamodb.update_table(
		        TableName="G_BadgeCollection",
		        AttributeDefinitions=[
		            {
		                "AttributeName": "applicant",
		                "AttributeType": "S"
		            },
		        ],
		        GlobalSecondaryIndexUpdates=[
		            {
		                "Create": {
		                    "IndexName": "applicantIndex",
		                    "KeySchema": [
		                        {
		                            "AttributeName": "applicant",
		                            "KeyType": "HASH"
		                        }
		                    ],
		                    "Projection": {
		                        "ProjectionType": "ALL"
		                    },
		                    "ProvisionedThroughput": {
		                        "ReadCapacityUnits": 2,
		                        "WriteCapacityUnits": 2,
		                    }
		                }
		            }
		        ],
		    )
		    print("Secondary index add!")
		except Exception as e:
		    print("Error updating table:")
		    print(e)

def G_BadgeCollection_GlobalSecondary_statusIndex(dynamodb):
		try:
		    response = dynamodb.update_table(
		        TableName="G_BadgeCollection",
		        AttributeDefinitions=[
		            {
		                "AttributeName": "status_event",
		                "AttributeType": "S"
		            },
		        ],
		        GlobalSecondaryIndexUpdates=[
		            {
		                "Create": {
		                    "IndexName": "statusIndex",
		                    "KeySchema": [
		                        {
		                            "AttributeName": "status_event",
		                            "KeyType": "HASH"
		                        }
		                    ],
		                    "Projection": {
		                        "ProjectionType": "ALL"
		                    },
		                    "ProvisionedThroughput": {
		                        "ReadCapacityUnits": 2,
		                        "WriteCapacityUnits": 2,
		                    }
		                }
		            }
		        ],
		    )
		    print("Secondary index add!")
		except Exception as e:
		    print("Error updating table:")
		    print(e)
