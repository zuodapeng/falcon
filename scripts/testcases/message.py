from uiautomator import device as d

import unittest, os, time

PACKAGE_NAME = 'com.android.mms'
ACTIVITY_NAME = '.ui.ConversationList'

MESSAGE_RECEIVER_NUMBER = '18610151492'
#max 160 characters
SEND_MESSAGE_CONTENT = 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest'


class MessagesTest(unittest.TestCase):
    def setUp(self):
        super(MessagesTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('home')
        super(MessagesTest, self).tearDown()

    def testSendSMS(self):
        """
        Summary:testSendSMS: Send a SMS.
        #Init condition:Clear up all messagebox
        Steps:1. Open Messages app
              2. Touch Compose button
              3. Input deliver number and content
              4. Touch Send button
              5. Delete all messages
              6. Exit Messages app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Messaging').wait.exists(), 'Message launch failed'

        self._clearMessage()

        #step2,3
        os.system('adb shell am start -a android.intent.action.SEND  --es address ' + MESSAGE_RECEIVER_NUMBER + ' --es sms_body ' + SEND_MESSAGE_CONTENT + ' -n com.android.mms/.ui.ComposeMessageActivity')
        time.sleep(2)

        #step4
        d(description = 'Send').click.wait()
        assert d(textContains = ':', className = 'android.widget.TextView').wait.exists(timeout = 35000), 'Message send failed'

        #step5
        d.press('back')
        self._clearMessage()

    # def testSendMMSWithAudio(self):
    #     """
    #     Summary:testSendMMSWithAudio: Send a MMS with audio attachment.
    #     #Init condition:Clear up all messagebox
    #     Steps:1. Open Messages app
    #           2. Touch Compose button
    #           3. Input deliver number and content
    #           4. Touch Attach button
    #           5. Select MyFiles
    #           6. Select the audio attach
    #           7. Touch Send button
    #           8. Select send by SIM1
    #           9. Delete all messages
    #           10. Exit Messages app
    #     """
    #     os.system('adb shell am start '+self.runComponent)
    #     assert d(text='Messaging').wait.exists(), 'Message launch failed'

    #     os.system('adb shell am start -a android.intent.action.SEND -t audio/* --es address '+ MESSAGE_RECEIVER_NUMBER +' --es sms_body '+ SEND_MESSAGE_CONTENT +' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Audio.mp3 -n com.android.mms/.ui.ComposeMessageActivity')
    #     time.sleep(2)

    #     d(description='Send MMS').click.wait()
    #     assert d(textContains=':', className='android.widget.TextView').wait.exists(timeout=60000), 'Message send failed'

    #     d.press('back')
    #     d.press('menu')
    #     d(text='Delete all threads').click.wait()
    #     d(text='Delete').click.wait()
    #     assert d(text='No conversations.').wait.exists(), 'message delete failed'


    def testSendMMSWithVideo(self):
        """
        Summary:testSendMMSWithVideo: Send a mms with video attachment.
        #Init condition:Clear up all messagebox
        Steps:1. Open Messages app
              2. Touch Compose button
              3. Input deliver number and content
              4. Touch Attach button
              5. Select Gallery
              6. Enter 001 folder, select a video
              7. Touch Send button
              8. Delete all messages
              9. Exit Messages app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Messaging').wait.exists(), 'Message launch failed'

        self._clearMessage()

        #step2,3,4,5,6
        os.system('adb shell am start -a android.intent.action.SEND -t video/* --es address ' + MESSAGE_RECEIVER_NUMBER + ' --es sms_body ' + SEND_MESSAGE_CONTENT + ' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Video.3gp -n com.android.mms/.ui.ComposeMessageActivity')
        assert d(text = 'View').wait.exists(), 'message create failed'

        #step7
        d(description = 'Send MMS').click.wait()
        assert d(textContains = ':', className = 'android.widget.TextView').wait.exists(timeout = 60000), 'Message send failed'

        #step8
        d.press('back')
        self._clearMessage()

    def testSendMMSWithImage(self):
        """
        Summary:testSendMMSWithImage: Send a mms with image attachment.
        #Init condition:Clear up all messagebox
        Steps:1. Open Messages app
              2. Touch Compose button
              3. Input deliver number and content
              4. Touch Attach button
              5. Select Gallery
              6. Enter 001 folder, select an image
              7. Touch Send button
              8. Delete all messages
              9. Exit Messages app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Messaging').wait.exists(), 'Message launch failed'

        self._clearMessage()

        #step2,3,4,5,6
        os.system('adb shell am start -a android.intent.action.SEND -t image/* --es address ' + MESSAGE_RECEIVER_NUMBER + ' --es sms_body ' + SEND_MESSAGE_CONTENT + ' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Picture.jpg -n com.android.mms/.ui.ComposeMessageActivity')
        assert d(text = 'View').wait.exists(), 'message create failed'

        #step7
        d(description = 'Send MMS').click.wait()
        assert d(textContains = ':', className = 'android.widget.TextView').wait.exists(timeout = 60000), 'Message send failed'

        #step8
        d.press('back')
        self._clearMessage()

    def testOpenSms(self):
        """
        Summary:testOpenSMS:open a sms
        #Init condition:Clear up all messagebox
        Precondition:
              1.Prepare a received sms.
        
        Steps:1.Launch Messages app
              2.Open a sms
              3.Delete message
              4.Exit message app
              
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Messaging').wait.exists(), 'Message launch failed'

        self._clearMessage()

        os.system('adb shell am start -a android.intent.action.SEND  --es address ' + MESSAGE_RECEIVER_NUMBER + ' --es sms_body ' + SEND_MESSAGE_CONTENT + ' -n com.android.mms/.ui.ComposeMessageActivity')
        time.sleep(2)
        d.press('back')

        #step2
        d(textContains = 'test').click.wait()
        assert d(description = 'Send').wait.exists(), 'SMS open failed'

        #step3
        d.press('back')
        d.press('back')
        self._clearMessage()

    # def testOpenMmsWithAudio(self):
    #     """
    #     Summary:testOpenMMSWithAudio:open a mms with audio
    #     #Init condition:Clear up all messagebox
    #     Precondition:
    #           1.There is a 600kb audio file in sdcard

    #     Steps:1.Launch message app
    #           2.Open a mms with audio 
    #           3.Delete message
    #           4.Exit message app
              
    #     """
    #     os.system('adb shell am start '+self.runComponent)
    #     assert d(text='Messaging').wait.exists(), 'Message launch failed'

    #     if d(text='No conversations.').wait.exists():
    #         assert True
    #     else:
    #         d.press('menu')
    #         d(text='Delete all threads').click.wait()
    #         d(text='Delete').click.wait()
    #         assert d(text='No conversations.').wait.exists(), 'message delete failed'

    #     os.system('adb shell am start -a android.intent.action.SEND -t audio/* --es address '+ MESSAGE_RECEIVER_NUMBER +' --es sms_body '+ SEND_MESSAGE_CONTENT +' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Audio.mp3 -n com.android.mms/.ui.ComposeMessageActivity')
    #     time.sleep(2)
    #     d.press('back')

    #     d(textContains='subject').click.wait()
    #     assert d(description='Send MMS').wait.exists(), 'MMS open failed'

    #     d.press('back')
    #     d.press('back')
    #     d.press('menu')
    #     d(text='Delete all threads').click.wait()
    #     d(text='Delete').click.wait()
    #     assert d(text='No conversations.').wait.exists(), 'message delete failed'

    def testOpenMmsWithVideo(self):
        """
        Summary:testOpenMmsWithVideo:open a mms with video
        #Init condition:Clear up all messagebox
        Precondition:
              1.There is a 600kb audio file in sdcard

        Steps:1.Launch message app
              2.Open a mms with audio 
              3.Delete message
              4.Exit message app
              
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Messaging').wait.exists(), 'Message launch failed'

        self._clearMessage()

        os.system('adb shell am start -a android.intent.action.SEND -t video/* --es address ' + MESSAGE_RECEIVER_NUMBER + ' --es sms_body ' + SEND_MESSAGE_CONTENT + ' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Video.3gp -n com.android.mms/.ui.ComposeMessageActivity')
        time.sleep(2)
        d.press('back')

        #step2
        d(textContains = 'subject').click.wait()
        assert d(description = 'Send MMS').wait.exists(), 'MMS open failed'

        #step3
        d.press('back')
        d.press('back')
        self._clearMessage()

    def testOpenMmsWithImage(self):
        """
        Summary:testOpenMmsWithVideo:open a mms with video
        #Init condition:Clear up all messagebox
        Precondition:
              1.There is a 600kb audio file in sdcard

        Steps:1.Launch message app
              2.Open a mms with audio 
              3.Delete message
              4.Exit message app      
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Messaging').wait.exists(), 'Message launch failed'

        self._clearMessage()

        os.system('adb shell am start -a android.intent.action.SEND -t image/* --es address ' + MESSAGE_RECEIVER_NUMBER + ' --es sms_body ' + SEND_MESSAGE_CONTENT + ' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Picture.jpg -n com.android.mms/.ui.ComposeMessageActivity')
        time.sleep(2)
        d.press('back')

        #step2
        d(textContains = 'subject').click.wait()
        assert d(description = 'Send MMS').wait.exists(), 'MMS open failed'

        #step3
        d.press('back')
        d.press('back')

        self._clearMessage()

    def _clearMessage(self):

        if d(text = 'No conversations.').wait.exists():
            assert True
        else:
            d.press('menu')
            d(text = 'Delete all threads').click.wait()
            d(text = 'Delete').click.wait()
            assert d(text = 'No conversations.').wait.exists(), 'message delete failed'


if __name__ == '__main__':  
    unittest.main()