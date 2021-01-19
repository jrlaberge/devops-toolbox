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


if __name__ == '__main__':
    unittest.main()
