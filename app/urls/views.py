from . import urls
import africastalking
from flask import redirect, url_for,render_template
from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# import urllib2
from .forms import Saccotext
from ..models import User


@urls.route('/url',methods=['GET','POST'])
def africa_talking():
    saccotext = Saccotext()
    if saccotext.validate_on_submit():

        users = User.query.all()
        print (users)
        usersNo. = users.phone_number
        
        
        # Specify your login credentials
        username ="m-fare"
        apiKey ="f6700eb3be26fd6dddf806920a93d98ff6dc14df98db4033a06a1aaea5434f70"
        # username = "sandbox"
        # apikey = "54a2cd06ea9b6118b691567a856ab4b92eeb3621e1b753e5f26815c967f44072"
        # Specify the numbers that you want to send to in a comma-separated list
        # Please ensure you include the country code (+254 for Kenya)

        to = usersNo
        # And of course we want our recipients to know what we really do

        message = saccotext.text.data
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
    return render_template('sms.html',saccotext=saccotext)