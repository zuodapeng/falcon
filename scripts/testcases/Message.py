#!/usr/bin/env python

from uiautomator import device as d

import unittest, os

PACKAGE_NAME = 'com.android.mms'
ACTIVITY_NAME = '.ui.ConversationList'

SMS_RECEIVER = '10010'
SMS_CONTENT = 'Test'


class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        d.wakeup()
        d.press('home')

    def tearDown(self):
        super(MessageTest, self).tearDown()
        d.press('back')
        d.press('back')
        d.press('home')

    def testSendSMS(self):
        '''
        1. Launch Message
        2. New a message
        3. Input receiver and content
        4. Send the sms
        5. Verify send successfully
        '''
        #step1
        os.system('adb shell am start ' + self.runComponent)
    	#d(text='Messaging').click.wait()
    	assert d(description = 'New message').wait.exists(), 'Message launch failed'
        #step2
    	d(description = 'New message').click.wait()
        #step3
        d(text = "To").set_text(SMS_RECEIVER)
        d(text = "Type message").set_text(SMS_CONTENT)
        d(description = "Send").click.wait()
        d.press('back')
        assert d(textContains = ':').wait.exists(timeout = 35000), 'SMS send failed'


if __name__ == '__main__':  
    unittest.main()