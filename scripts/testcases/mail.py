from uiautomator import device as d

import unittest, os, commands

PACKAGE_NAME = 'com.android.email'
ACTIVITY_NAME = PACKAGE_NAME + '.activity.Welcome'

RECEIVER_ADDRESS = 'limanxy1@126.com'
SUBJECT = 'Subjectsubject'
CONTEXT = 'Testtest'

class MailTest(unittest.TestCase):
    def setUp(self):
        super(MailTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(MailTest, self).tearDown()

    def testMailSendWithoutAttachment(self):

        """
        Summary:testSendMailWithoutAttach: send mail without attachment.
        Steps:1.Launch email app
              2.Clear up all mailbox 
              3.Create a new mail
              4.Send mail
              5.Check send succesfully
              6.Delete the sended mail
              7.Exit email app
        """
        #step1
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Compose').wait.exists(), 'Email launch failed'

        #step2
        d(description = 'Show all folders').click.wait()
        d(text = 'Sent').click.wait()
        while d(descriptionContains = 'Subject').wait.exists():
            d.click(30,170)
            d(description = 'Delete').click.wait(timeout = 1000)

        #step3
        commands.getoutput('adb shell am start -a android.intent.action.SEND -d mailto:' + RECEIVER_ADDRESS + ' --es android.intent.extra.SUBJECT ' + SUBJECT + ' --es android.intent.extra.TEXT ' + CONTEXT + ' -n com.android.email/.activity.MessageCompose')
        assert d(text = 'Compose').wait.exists()

        #step4
        d(description = 'Send').click.wait(timeout = 3000)

        #step5
        d(description = 'Show all folders').click.wait()
        d(text = 'Sent').click.wait()
        assert d(descriptionContains = 'Subject').wait.exists(timeout = 90000), 'Email sent failed'

        #step6
        d(descriptionContains = 'Subject').long_click().wait()
        assert d(description = 'Delete').wait.exists(), 'Email did not selected'
        d(description = 'Delete').click.wait()
        assert d(text = 'No messages').wait.exists, 'Email delete failed'

    def testMailSendwithAttachment(self):

        """
        Summary:testSendMailWithAttach: send mail with attachment.
        Steps:1.Launch email app
              2.Clear up all mailbox 
              3.Create a new mail with attachment(image)
              4.Send mail
              5.Check send succesfully
              6.Delete the sended mail
              7.Exit email app
        """
        #step1
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Compose').wait.exists(), 'Email launch failed'

        #step2
        d(description = 'Show all folders').click.wait()
        d(text = 'Sent').click.wait()
        while d(descriptionContains = 'Subject').wait.exists():
            d.click(30,170)
            d(description = 'Delete').click.wait(timeout = 1000)

        #step3
        commands.getoutput('adb shell am start -a android.intent.action.SEND -d mailto:' + RECEIVER_ADDRESS + ' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Picture.jpg --es android.intent.extra.SUBJECT ' + SUBJECT + ' --es android.intent.extra.TEXT ' + CONTEXT + ' -n com.android.email/.activity.MessageCompose')
        assert d(text = 'Compose').wait.exists(), 'Email with attachment create failed'

        #step4
        d(description = 'Send').click.wait(timeout = 3000)

        #step5
        d(description = 'Show all folders').click.wait()
        d(text = 'Sent').click.wait()
        assert d(descriptionContains = 'Subject').wait.exists(timeout = 90000), 'Email sent failed'

        #step6
        d(descriptionContains = 'Subject').long_click().wait()
        assert d(description = 'Delete').wait.exists(), 'Email did not selected'
        d(description = 'Delete').click.wait()
        assert d(text = 'No messages').wait.exists, 'Email delete failed'

    def testOpenMail(self):
        """
        Summary:testOpenMail: test open mail.
        Steps:1.Launch email app
              2.Clear up all mailbox 
              3.Create a new mail with attachment(image)
              4.Check mail context
              5.Save as draft
              6.Open the draft mail
              7.Check mail context,subject and so on
              8.Delete all mail
              9.Exit mail app
        """
        #step1
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Compose').wait.exists(), 'Email launch failed'

        #step2
        d(description = 'Show all folders').click.wait()
        d(text = 'Drafts').click.wait()
        while d(descriptionContains = 'Subject').wait.exists():
            d.click(30,170)
            d(description = 'Delete').click.wait(timeout = 1000)

        #step3
        commands.getoutput('adb shell am start -a android.intent.action.SEND -d mailto:' + RECEIVER_ADDRESS + ' --eu android.intent.extra.STREAM file:///mnt/sdcard/001/300K/Picture.jpg --es android.intent.extra.SUBJECT ' + SUBJECT + ' --es android.intent.extra.TEXT ' + CONTEXT + ' -n com.android.email/.activity.MessageCompose')
        assert d(text = 'Compose').wait.exists(), 'Email with attachment create failed'

        #step4
        d.press('back')
        d.press('back')

        #step5
        d(description = 'Show all folders').click.wait()
        d(text = 'Drafts').click.wait()

        #step6
        assert d(descriptionContains = 'Subject').wait.exists(), 'No Email in Drafts'

        #step7
        d(descriptionContains = 'Subject').click.wait()
        assert d(description = 'Send').wait.exists(), 'Email open failed'

        #step8
        d.press('back')
        d.press('back')
        d(descriptionContains = 'Subject').long_click().wait()
        assert d(description = 'Delete').wait.exists(), 'Email did not selected'
        d(description = 'Delete').click.wait()
        assert d(text = 'No messages').wait.exists, 'Email delete failed'


if __name__ == '__main__':  
    unittest.main()