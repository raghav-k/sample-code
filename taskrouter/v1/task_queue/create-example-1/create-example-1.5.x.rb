# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

task_queue = @client.taskrouter
  .workspaces('WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
  .task_queues
  .create(
     assignment_activity_sid: 'WA21d51f4c72583766988f9860de3e130a',
     reservation_activity_sid: 'WAea296a56ebce4bfbff0e99abadf16934',
     target_workers: 'languages HAS "english"',
     friendly_name: 'English'
   )

puts task_queue.sid
