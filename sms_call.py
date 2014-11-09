import twilio
import twilio.rest
from twilio import twiml

def send_sms(text,to):
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC87d4a57db8293e616adc704a088a73c7"
	auth_token  = "c73125f8b1d65343107ecb54f0d12bc8"
	try:
		client = twilio.TwilioRestClient(account_sid, auth_token)
		message = client.messages.create(body=text,to=to,from_ = "+12136341902")
		return message.sid
	except twilio.TwilioRestException as e:
		print e
	


def make_call(title,start,to):
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC87d4a57db8293e616adc704a088a73c7"
	auth_token  = "c73125f8b1d65343107ecb54f0d12bc8"
	try:
		client = twilio.TwilioRestClient(account_sid, auth_token)
		r = twiml.Response()
		r.say("The event "+title+" will start at "+start)
		output = open("words.xml",'w')
		output.write(r.toxml())
		output.close()
		call = client.calls.create(to=to, from_="+12136341902",url="./words.xml")
		print call.length
		return call.sid
	except twilio.TwilioRestException as e:
		print e









