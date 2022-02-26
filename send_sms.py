from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
import json
from datetime import datetime
import sys
import time

try:
	client = Client(account_sid, auth_token)
except:
	print("Couldn't connect to client")
	sys.exit()

def send_wish(name, occasion, to_phone, to_message, from_message, client):
	message_body = f"Wish Reminder: Send {occasion} wishes to your dearest friend {name} their contact {to_phone}."
	try:
		message = client.messages.create(to=my_cell, from_=my_twilio, body=message_body)
    print("Hey! my friendship is saved. :) :)")
	except:
		print("Your friendship is in danger. :( :(")

# reading in the json file
with open("wishes.json") as json_file:
	data = json.load(json_file)
	# iterating over date
	today = datetime.today()
	today_date = f"{today.strftime('%B')} {today.day}" # example March 25
	for date in data:
		if today_date == date:
			occasions = data[today_date]
			# iterate over all occasion types
			for occasion in occasions:
				for each_person in occasions[occasion]:
					send_wish(each_person["name"], occasion,
							each_person["phone"],
							each_person["to_message"],
							each_person["from_message"], client)
					time.sleep(1) # wait for a second before next message
