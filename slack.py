#!/usr/local/bin/python3
# Author: Jon Laberge

import os 
import logging
import sys
import json

from decouple import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s %(module)s %(message)s')

class SlackClient:
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
            logging.info(f"Message: {response['message']['ts']} has been posted successfully.")
            return response
        except SlackApiError as e:
            logging.error(f"Error received {e.response['error']}")
            return e.response


    def delete_message(self, channel, message_id):
        """Delete a message from Slack

        Parameters:
        channel (String): Which channel to post message to, this can be #channel or @userid
        message_id (Integer): Message ts ie. <1610858384.007400>

        OAuth Scopes Required:
        ---
        chat:write
        """

        try:
            response = self.client.chat_delete(channel=channel, ts=message_id)
            logging.info(f"Message: {response['ts']} has been deleted successfully.")
            return response
        except SlackApiError as e:
            logging.error(f"Error received {e.response['error']}")
            return e.response

    def update_message(self, channel, message_id, text):
        """ Update a Slack message

        Parameters:
        channel (String): Which channel to post message to, this can be #channel or @userid
        message_id (Integer): Message ts ie. <1610858384.007400>
        text (String): New content that will replace the existing content.

        OAuth Scopes Required:
        ---
        chat:write
        """

        try:
            response = self.client.chat_update(channel=channel, ts=message_id, text=text)
            logging.info(f"Message: {response['ts']} has been updated successfully.")
            return response
        except SlackApiError as e:
            logging.error(f"Error received {e.response['error']}")
            return e.response


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
            logging.info(f"File: {response['file']['id']} has been uploaded successfully.")
            return response
        except SlackApiError as e:
            logging.error(f"Error received {e.response['error']}")
            return e.response

    
    def delete_file(self, file_id):
        """ Deletes a file that was uploaded to Slack

        Parameters:
        file_id (String): ID of the file to delete

        OAuth Scopes Required:
        ---
        files:write
        """

        try:
            response = self.client.files_delete(file=file_id)
            logging.info(f"File: {file_id} has been deleted successfully.")
            return response
        except SlackApiError as e:
            logging.error(f"Error received {e.response['error']}")
            return e.response


if __name__ == '__main__':
    # Sample usage

    # create slack object
    slack = SlackClient()

    # send a message, store the response
    msg = slack.send_message(channel='@jrlaberge91', text='this is a test!')

    # get channel id from response
    channel = msg['channel']

    # get message id from response
    message_id = msg['message']['ts']

    # update the message that was sent previously
    slack.update_message(channel, message_id, 'updating my previous message')

    # delete the message that was sent previously
    slack.delete_message(channel, message_id)

    # upload a file, store the response
    upload = slack.upload_file(channel='@jrlaberge91', filepath='./README.md')

    # get file id from the response
    file_id = upload['file']['id']

    # delete the file that was uploaded
    slack.delete_file(file_id)