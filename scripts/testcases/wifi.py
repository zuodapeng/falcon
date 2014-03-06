from uiautomator import device as d

import unittest, os, time

PACKAGE_NAME = 'com.android.settings'
ACTIVITY_NAME = PACKAGE_NAME + '.Settings'

class WifiTest(unittest.TestCase):
    def setUp(self):
        super(WifiTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(WifiTest, self).tearDown()

    def testWifiOpenAndClose(self):
        """
        Summary:testWifiRadioTurnOffAndOn: Turn wifi off and on.
        Pre-conditions:
        1. Wifi is radio off        
        Steps:1. Open Settings app
              2. Touch Wifi button to turn on Wifi
              3. Touch Wifi button to turn off Wifi
              4. Exit Settings app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Settings').wait.exists(), 'Setting launch failed'

        #step2,3
        d(text = 'Wi-Fi').click.wait()
        if d(text = 'To see available networks, turn Wi-Fi on.').wait.exists():
            d(text = 'OFF').click.wait()
            assert d(text = 'ON').wait.exists(), 'Wi-Fi turn on failed'
            d(text = 'ON').click.wait()
            assert d(text = 'OFF').wait.exists(), 'Wi-Fi turn off failed'
        else:
            d(text = 'ON').click.wait()
            assert d(text = 'OFF').wait.exists(), 'Wi-Fi turn off failed'
            d(text = 'OFF').click.wait()
            assert d(text = 'ON').wait.exists(), 'Wi-Fi turn on failed'
            d(text = 'ON').click.wait()
            assert d(text = 'OFF').wait.exists(), 'Wi-Fi turn off failed'

        """
        if d(text='Wi-Fi').right(text='ON').wait.exists():
            d(text='Wi-Fi').right(text='ON').click.wait()
            d(text='Wi-Fi').right(text='OFF').click.wait()
            assert d(text='Wi-Fi').right(text='ON').wait.exists(), 'Wi-Fi turn on'
            d(text='Wi-Fi').right(text='ON').click.wait()
            assert d(text='Wi-Fi').right(text='OFF').wait.exists(), 'Wi-Fi turn off'
        else:
            d(text='Wi-Fi').right(text='OFF').click.wait()
            assert d(text='Wi-Fi').right(text='ON').wait.exists(), 'Wi-Fi turn on'
            d(text='Wi-Fi').right(text='ON').click.wait()
            assert d(text='Wi-Fi').right(text='OFF').wait.exists(), 'Wi-Fi turn off'
        """


if __name__ == '__main__':  
    unittest.main()
