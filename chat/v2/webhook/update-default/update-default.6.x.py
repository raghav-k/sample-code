# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

webhook = client.chat.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .channels('CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .webhooks('WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .update(configuration_url='configuration_url')

print(webhook.sid)
