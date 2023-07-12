import slack
import os
from dotenv import load_dotenv
from listfromcsv import csvtolist

load_dotenv()

API_TOKEN = os.getenv('GETUSER_TOKEN')
client=slack.WebClient(API_TOKEN)

def getuserID():  #this function reads the list of emails and calls to Slack to get the actual userIDs. this is necessary to open a direct channel with users
    email_list = csvtolist() 
    userIDs = []
    i=0
    for each in email_list:
        userIDparam = client.users_lookupByEmail(email = email_list[i])['user']['id']
        userIDs.append(userIDparam)
        i = i+1
    return userIDs