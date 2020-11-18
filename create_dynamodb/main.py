import time

import boto3

from src.Feedback import *
from src.G_BadgeCollection import *
from src.G_RankingCompetition import *
from src.LT_DailyTask import *
from src.LT_MonthlyGift import *
from src.Personal_Data import *
from src.Transaction_History import *


account_type = input('''
	Choose account type:
	1. AWS account
	2. AWS Educate account
	enter number: ''')
aws_access_key_id = input("Please enter aws access key id:")
aws_secret_access_key = input("Please enter aws secret access key:")

if aws_access_key_id == '' or aws_secret_access_key == '':
	print("Please enter correct info.")
else:
	if account_type == '2':
		aws_session_token = input("Please enter aws session token:")
		if aws_session_token == '':
			print("Please enter correct info.")

		else:

			dynamodb = boto3.resource('dynamodb', region_name='us-east-1',\
			                  aws_access_key_id = aws_access_key_id,\
			                  aws_secret_access_key = aws_secret_access_key,\
			                  aws_session_token = aws_session_token)

			dynamodb_client = boto3.client('dynamodb', region_name='us-east-1',\
			                          aws_access_key_id = aws_access_key_id,\
			                          aws_secret_access_key = aws_secret_access_key,\
			                          aws_session_token = aws_session_token)

			while True:
				var_table = input("""
					Please chose table:
					1. Feedback
					2. G_BadgeCollection
					3. G_RankingCompetition
					4. LT_DailyTask
					5. LT_MonthlyGift
					6. Personal_Data
					7. Transaction_History
					enter number: """)

				if var_table in ['2', '4', '5', '7']:
					var_function = input("""
						Please chose function: 
						1. create table
						2. add index
						enter number: """)
				elif var_table in ['1', '3', '6']:
					var_function = input("""Please chose function: 
						1. create table
						enter number: """)
				else:
					print("Please enter correct number!")


				if var_table == '1':
					"""Feedback"""

					if var_function == '1':
						Feedback(dynamodb)
					else:
						print("Please enter correct number!")

				elif var_table == '2':
					"""G_BadgeCollection"""

					if var_function == '1':
						G_BadgeCollection(dynamodb)
					elif var_function == '2':
						index = input('''
							add index:
							1. applicantIndex
							2. statusIndex
							enter number: ''')
						if index == '1':
							G_BadgeCollection_GlobalSecondary_applicantIndex(dynamodb_client)
							time.sleep(5)
						elif index == '2':
							G_BadgeCollection_GlobalSecondary_statusIndex(dynamodb_client)
							time.sleep(5)
						else:
							print("Please enter correct number!")
					else:
						print("Please enter correct number!")

				elif var_table == '3':
					"""G_RankingCompetition"""

					if var_function == '1':
						G_RankingCompetition(dynamodb)

					else:
						print("Please enter correct number!")

				elif var_table == '4':
					"""LT_DailyTask"""

					if var_function == '1':
						LT_DailyTask(dynamodb)
					elif var_function == '2':
						index = input('''
							add index:
							1. dateIndex
							2. statusIndex
							enter number: ''')
						if index == '1':
							LT_DailyTask_GlobalSecondary_dateIndex(dynamodb_client)
							time.sleep(5)
						elif index == '2':
							LT_DailyTask_GlobalSecondary_statusIndex(dynamodb_client)
							time.sleep(5)
						else:
							print("Please enter correct number!")
					else:
						print("Please enter correct number!")

				elif var_table == '5':
					"""LT_MonthlyGift"""

					if var_function == '1':
						LT_MonthlyGift(dynamodb)
					elif var_function == '2':
						ndex = input('''
							add index:
							1. periodIndex
							enter number: ''')
						if index == '1':
							LT_MonthlyGift_GlobalSecondary(dynamodb_client)
							time.sleep(5)
						else:
							print("Please enter correct number!")
					else:
						print("Please enter correct number!")

				elif var_table == '6':
					"""Personal_Data"""

					if var_function == '1':
						Personal_Data(dynamodb)

					else:
						print("Please enter correct number!")

				elif var_table == '7':
					"""Transaction_History"""

					if var_function == '1':
						Transaction_History(dynamodb)
					elif var_function == '2':
						index = input('''
							add index:
							1. receiverIndex
							2. senderrIndex
							enter number: ''')
						if index == '1':
							Transaction_History_GlobalSecondary_receiverIndex(dynamodb_client)
							time.sleep(5)
						elif index == '2':
							Transaction_History_GlobalSecondary_senderrIndex(dynamodb_client)
							time.sleep(5)
						else:
							print("Please enter correct number!")
					else:
						print("Please enter correct number!")

				else:
					print("Please enter correct number!")

				stop = input('''
					Do you want to continue?
					1. Yes
					2. No
					enter number: ''')

				if stop == '2':
					break




