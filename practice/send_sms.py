
from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException


#client = TwilioRestClient(account='AC38135355602040856210245275870',
 #                             token='2flnf5tdp7so0lmfdu3d')
client = TwilioRestClient()

try:
	client.messages.create(to="<your cell num>", from_="+15104564545",
			body="Hey Shrikant this is python message")
except TwilioRestException as e:
	print(e)


