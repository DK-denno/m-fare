# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
#Specify your credentials
username = "MyAppUsername"
apiKey   = "MyAppApiKey"
#Create an instance of our awesome gateway class and pass your credentials
gateway = AfricasTalkingGateway(username, apiKey, "sandbox")
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
# Specify the name of your Africa's Talking payment product
productName  = "My Online Store"
# The phone number of the customer checking out
phoneNumber  = "+254711XXXYYY"
# The 3-Letter ISO currency code for the checkout amount
currencyCode = "KES"
# The checkout amount
amount       = 100.50
# Any metadata that you would like to send along with this request
# This metadata will be  included when we send back the final payment notification
metadata     = {"agentId"   : "654",
                "productId" : "321"}
try:
    # Initiate the checkout. If successful, you will get back a transactionId
    transactionId = gateway.initiateMobilePaymentCheckout(productName,
                              phoneNumber,
                              currencyCode,
                              amount,
                              metadata)
    print "The transactionId is " + transactionId
    
except AfricasTalkingGatewayException, e:
    print "Received error response: %s" % str(e)