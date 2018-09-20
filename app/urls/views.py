from . import urls
from flask import redirect, url_for
from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# import urllib2


@urls.route('/url')
def africa_talking():
    # Specify your login credentials
    username = "mfare"
    apiKey = "9e2800c8091653946a0a49a50a9db4ca9c0788e0558f7ac266c5da0fecb42703"
    # username = "sandbox"
    # apikey = "54a2cd06ea9b6118b691567a856ab4b92eeb3621e1b753e5f26815c967f44072"
    # Specify the numbers that you want to send to in a comma-separated list
    # Please ensure you include the country code (+254 for Kenya)

    to = "+254725328016"
    # And of course we want our recipients to know what we really do

    message = "random txt"
    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apiKey)
    # *************************************************************************************
    #  NOTE: If connecting to the sandbox:
    #
    #  1. Use "sandbox" as the username
    #  2. Use the apiKey generated from your sandbox application
    #     https://account.africastalking.com/apps/sandbox/settings/key
    #  3. Add the "sandbox" flag to the constructor
    #
    #  gateway = AfricasTalkingGateway(username, apiKey, "sandbox");
    # **************************************************************************************
    # Any gateway errors will be captured by our custom Exception class below,
    # so wrap the call in a try-catch block
    try:
        # Thats it, hit send and we'll take care of the rest.

        results = gateway.sendMessage(to, message)
        print(results)

        for recipient in results:
            # status is either "Success" or "error message"
            print('number= %s;status= %s;statusCode= %s;messageId= %s;cost= %s' % (
                recipient['number'], recipient['status'], recipient['statusCode'], recipient['messageId'], recipient['cost']))
    except AfricasTalkingGatewayException as e:
        print('Encountered an error while sending: %s' % str(e))

    return redirect(url_for('main.index'))
