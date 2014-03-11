from uiautomator import device as d

import unittest, os, random, commands

NETWORK_PACKAGE_NAME = 'com.android.phone'

NETWORK_MODE_COMPONENT = NETWORK_PACKAGE_NAME + '.MobileNetworkSettings'

class NetworkTest(unittest.TestCase):
    def setUp(self):
        super(NetworkTest, self).setUp()
        self.runComponent = NETWORK_PACKAGE_NAME + '/' + NETWORK_MODE_COMPONENT

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(NetworkTest, self).tearDown()

    def testSwitchTo2GOnlyNerwork(self):
        """
        Summary:testSwitchTo2GOnlyNerwork: Switch network to 2G.
        Steps:1. Open mobile network setting
              2. Check if in 2G mode
              3. If not enter only 2G mode
        """
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(text = 'Mobile network settings').wait.exists(), 'Mobile network settings launch failed'

        if d(text = 'Use only 2G networks').right(checked = 'true').wait.exists():
            pass
        else:
            d(text = 'Use only 2G networks').right(className = 'android.widget.CheckBox').click.wait()
            assert d(text = 'Use only 2G networks').right(checked = 'true').wait.exists()


if __name__ == '__main__':  
    unittest.main()