#!/usr/local/bin/python3
# Author: Jon Laberge

import unittest

from devops_toolbox.common.slack import SlackClient

class TestSlack(unittest.TestCase):

    slack = SlackClient()
    
    def setUp(self):
        self.message_id = None
        self.channel_id = None

    def test_send_message(self):
        """ Test sending a message
        """
        
        msg = self.slack.send_message('@jrlaberge91', 'testing')
        self.message_id = msg['message']['ts']
        self.channel_id = msg['channel']

        self.assertTrue(msg['ok'])

    def test_update_message(self):
        """ Test updating a message
        """

        updated = self.slack.update_message(self.channel_id, self.message_id, text='This is updated text')
        self.assertTrue(updated['ok'])


    def test_delete_message(self):
        """ Test deleting a message
        """

        deleted = self.slack.delete_message(self.channel_id, self.message_id)
        self.assertTrue(deleted['ok'])


if __name__ == '__main__':
    unittest.main()
