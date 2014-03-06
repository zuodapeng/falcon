#!/usr/bin/env python

from uiautomator import device as d

import unittest, os


PACKAGE_NAME = 'com.android.browser'
ACTIVITY_NAME = '.BrowserActivity'


class BrowserTest(unittest.TestCase):
    def setUp(self):
        super(BrowserTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        d.wakeup()
        d.press('home')

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('home')
        super(BrowserTest, self).tearDown()

    def testBrowserLaunchAndClose(self):
        """
        Summary:testBrowserLaunchHomePage: Open and close Browser.
        Init Condition:
              1.Clear browser cache.
        Steps:1.Launch Browser and check launch successfully
        """
        #step1
        os.system('adb shell am start '+self.runComponent)
        d.press('menu')
    	assert d(text='Bookmarks').wait.exists(), 'Browser launch failed'



if __name__ =='__main__':  
    unittest.main()