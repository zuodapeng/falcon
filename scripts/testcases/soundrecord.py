from uiautomator import device as d

import unittest, os

PACKAGE_NAME = 'com.android.soundrecorder'
ACTIVITY_NAME = '.SoundRecorder'

class ContactTest(unittest.TestCase):
    def setUp(self):
        super(ContactTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(ContactTest, self).tearDown()

    def testRecordMessage(self):       
        """
        Summary:testRecordMessage: Record a message 5s.
        Init condition:Clear up all record which in record folder
        Steps:1. Open soundrecord app
              2. Touch record button to record message
              3. Touch stop button to stop record 
              4. Touch save button
              5. Exit Music app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Record your message').wait.exists(), 'SoundRecorder launch failed'

        #Step2
        d(index = 0, className = 'android.widget.ImageButton').click.wait(timeout = 5000)
        assert d(text = 'Recording').wait.exists(), 'not recording'
        #step3
        d(index = 2, className = 'android.widget.ImageButton').click.wait()
        assert d(text = 'Done').wait.exists(), 'recording save failed'
        #step4
        d(text = 'Done').click.wait()


if __name__ == '__main__':  
    unittest.main()

