# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

worker_channel = client.taskrouter \
                       .workspaces('WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .workers('WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .worker_channels('WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .fetch()

print(worker_channel.task_channel_unique_name)
