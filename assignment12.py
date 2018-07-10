#q.no.1

#Access tokens are the thing that applications use to make API requests on behalf of a user.
#The access token represents the authorization of a specific application to access specific parts of a user's data

access_token="RPqKCVQsmW1rDRvqneYwOIUpguxPH6GIqgyzrwC962KVV"


#q.no.2
""
import socket
print (socket.gethostbyname("www.amazon.in"))


#q.no.3

from keys import consumer_key,consumer_secret,access_secret,access_token
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_secret,access_token)
api = tweepy.API(oauth)
print(api.search("#MCCC"))

#Q.NO.4
#Difference between a library and an API
#API is a part of library which defines how an application communicates with external code
#API can be written in any language.
#Library is written in same language which is a collection of all the functionalities required for the use case
#For example numpy is a library of python

#Q.NO.5

import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("gupta.danish236@gmail.com")
to_email = Email("balwantrawat333@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
