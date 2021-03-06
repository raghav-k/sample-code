# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

events = @client.monitor.events.list(
                                  end_date: Date.new(2015, 4, 25),
                                  source_ip_address: '104.14.155.29',
                                  start_date: Date.new(2015, 4, 25)
                                )

events.each do |record|
  puts record.sid
end
