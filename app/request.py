# from .models import User
# from . import africastalkinggateway,africastalkinggatewayexception
# def Api_call():
#     # Import the helper gateway class

#     # Specify your credentials
#     username = "sandbox"
#     apiKey = "4aeb3e93b58958599b526c818596631247d0657d3fadb9746dde650227ca63d4"
#     # Create an instance of our awesome gateway class and pass your credentials
#     gateway = AfricasTalkingGateway(username, apiKey, "sandbox")
#     # *************************************************************************************
#     #  NOTE: If connecting to the sandbox:
#     #
#     #  1. Use "sandbox" as the username
#     #  2. Use the apiKey generated from your sandbox application
#     #     https://account.africastalking.com/apps/sandbox/settings/key
#     #  3. Add the "sandbox" flag to the constructor
#     #
#     #  gateway = AfricasTalkingGateway(username, apiKey, "sandbox");
#     # **************************************************************************************
#     # Specify the name of your Africa's Talking payment product
#     productName = "M-fare"
#     # The phone number of the customer checking out
#     phoneNumber = "+254725328016"
#     # The 3-Letter ISO currency code for the checkout amount
#     currencyCode = "KES"
#     # The checkout amount
#     amount = 1.00
#     # Any metadata that you would like to send along with this request
#     # This metadata will be  included when we send back the final payment notification
#     metadata = {"agentId": "654",
#                 "productId": "321"}
#     try:
#         # Initiate the checkout. If successful, you will get back a transactionId
#         transactionId = gateway.initiateMobilePaymentCheckout(productName,
#                                                               phoneNumber,
#                                                               currencyCode,
#                                                               amount,
#                                                               metadata)
#         print ("The transactionId is " + transactionId)


#     except AfricasTalkingGatewayException, e:
#         print ("Received error response: %s" % str(e))

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