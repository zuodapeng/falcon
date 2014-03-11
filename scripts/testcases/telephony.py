from uiautomator import device as d

import unittest, os, random, commands

PACKAGE_NAME = 'com.android.contacts'
ACTIVITY_NAME = '.activities.DialtactsActivity'

class TelephonyTest(unittest.TestCase):
    #get device
    def setUp(self):
        super(TelephonyTest,self).setUp()
        d.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(TelephonyTest,self).tearDown()

    def testCallFromPhoneBook(self):
        """
        Summary:testCallFromPhoneBook: Make a call from phonebook.
        Steps:1. Launch phone app
              2. Touch Contacts tab
              3. Touch the first contact
              4. Touch call button to make a call
              5. End the call
              6. Exit Phone app
        """
        #step1
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Favorites and all contacts').wait.exists(), 'Phone launch failed'
        #step2
        d(description = 'Favorites and all contacts').click.wait()
        #step3,4
        for i in range (random.randint(1,5)):
            d.swipe(196,700,196,180,steps = 10)
      
        for i in range (random.randint(1,5)):
            d.swipe(196,180,196,700,steps = 10)

        d.click(random.randint(130,370),random.randint(217,871))
        assert d(text = 'Dialing').wait.exists(timeout = 15000), 'Not start to call'
        assert d(textContains = '0:').wait.exists(timeout = 15000), 'Call is not connected'
        #step5
        d(description = 'End').click.wait()
        assert d(description = 'Favorites and all contacts').wait.exists(), 'Call end failed'


    def testCallFromCallLog(self):
        """
        Summary:testCallFromCallLog: Make a call from callLog.
        Init:clear up all callLog and insert a callLog.
        Steps:1. Open Phone app
              2. Touch Logs tab
              3. Touch the first call log to make a call
              4. End the call
              5. Exit Phone app
        """
        #step1
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Call log').wait.exists(), 'Phone launch failed'
        #step2
        d(description = 'Call log').click.wait()
        assert d(textContains = 'test').wait.exists(), 'no callLog'
        #step3
        d(textContains = 'test').click.wait()
        assert d(textContains = 'Call').wait.exists(), 'callLog detail launched'

        d(textContains = 'Call').click.wait()

        assert d(text = 'Dialing').wait.exists(timeout = 15000), 'Not start to call'
        assert d(textContains = '0:').wait.exists(timeout = 15000), 'Call is not connected'
        #step4
        d(description = 'End').click.wait()
        assert d(description = 'Call log').wait.exists(), 'Call end failed'

if __name__ == '__main__':  
    unittest.main()


