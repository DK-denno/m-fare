# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# Specify your login credentials
username = "M-fare"
apikey   = "MyAppAPIKey"
# Specify the numbers that you want to send to in a comma-separated list
# Please ensure you include the country code (+254 for Kenya)
to      = "+254711XXXYYY,+254733YYYZZZ"
# And of course we want our recipients to know what we really do
message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)
#*************************************************************************************
#  NOTE: If connecting to the sandbox:
#
#  1. Use "sandbox" as the username
#  2. Use the apiKey generated from your sandbox application
#     https://account.africastalking.com/apps/sandbox/settings/key
#  3. Add the "sandbox" flag to the constructor
#
#  gateway = AfricasTalkingGateway(username, apiKey, "sandbox");
#**************************************************************************************
# Any gateway errors will be captured by our custom Exception class below, 
# so wrap the call in a try-catch block
try:
    # Thats it, hit send and we'll take care of the rest.
    
    results = gateway.sendMessage(to, message)
    
    for recipient in results:
        # status is either "Success" or "error message"
        print 'number=%s;status=%s;statusCode=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                            recipient['status'],
                                                            recipient['statusCode'],
                                                            recipient['messageId'],
                                                            recipient['cost'])
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while sending: %s' % str(e)