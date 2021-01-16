#!/usr/local/bin/python3
# Author: Jon Laberge

import os 

from decouple import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackApi():
    def __init__(self):
        self.client = WebClient(token=config('SLACK_BOT_TOKEN'))


    def send_message(self, channel, text):
        """ Send a Slack message

        Parameters:
        channel (String): Which channel to post message to, this can be #channel or @userid
        text (String): The content of the message to send

        OAuth Scopes Required:
        ---
        chat:write
        """
        
        try:
            response = self.client.chat_postMessage(channel=channel, text=text)
        except SlackApiError as e:
            print(f"Got an error: {e.response['error']}")
            return e.response['ok']


    def upload_file(self, channel, filepath):
        """ Uploads a file to Slack

        Parameters:
        channel (String): Which channel to post message to, this can be #channel or @userid
        filepath (String): The path to the file (relative paths are OK)

        OAuth Scopes Required:
        ---
        files:write
        """

        try:
            response = self.client.files_upload(channels=channel, file=filepath)
            return response['ok']
        except SlackApiError as e:
            print(f"Got an error: {e.response['error']}")
            return e.response['ok']

if __name__ == '__main__':
    slack = SlackApi()
    slack.send_message(channel='@username', text='this is a test!')
    slack.upload_file(channel='@username', filepath='./README.md')
