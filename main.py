import os
import slack
from dotenv import load_dotenv
from useridlist import getuserID

load_dotenv()

USER_TOKEN = os.getenv('DMUSER_TOKEN') #Sends as me
BOT_USER_TOKEN = os.getenv('BOT_DMUSER_TOKEN') #Sends as Bot, bot needs to be added to channel
MESSAGE_TEXT = os.getenv('MESSAGE_TEXT') #Sends message text string currently in env file. 

client=slack.WebClient(USER_TOKEN)

user_list = getuserID()
i = 0

for each in user_list: #this will open a conversation with each user and send to them as a Direct Message
    client.chat_postMessage(channel = user_list[i], text = MESSAGE_TEXT)
    i = i+1