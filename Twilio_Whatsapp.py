from twilio.rest import Client 
 
account_sid = 'AC9f26dc52de95bf48c2f6c6b19018e13e' 
auth_token = '4725908e9b94366b5f1c573636f0416b' 
client = Client(account_sid, auth_token) 
 
n = 0
def spam():
	message = client.messages.create( 
	                              from_='whatsapp:+14155238886',  
	                              body='You are cool, but i am a bot.\n I will spam you every 2secs.',     
	                              to='whatsapp:+917039502646' 
	                          ) 
	
	print(message.sid)

#917304163367 shivam number

#14155238886 sender server