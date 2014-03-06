#!/usr/bin/env python

from uiautomator import device as d

import unittest, time, os

PACKAGE_NAME = 'com.android.contacts'
ACTIVITY_NAME = '.activities.DialtactsActivity'


class PhoneTest(unittest.TestCase):
    def setUp(self):
        super(PhoneTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        d.wakeup()
        d.press('home')

    def tearDown(self):
        super(PhoneTest, self).tearDown()
        d.press('back')
        d.press('back')
        d.press('home')

    def testMoCall(self):
        '''
        1. Launch Phone
        2. Switch to Dialer
        3. input 10010 and dial
        4. connect and wait for 10s
        5. end Call
        '''
        #step1
    	#d(text='Phone').click.wait()
        os.system('adb shell am start '+self.runComponent)
    	assert d(description='Phone').wait.exists(), 'Dialer launch failed'
        #step2
    	d(description='Phone').click.wait()
        #step3
    	d(description='one').click.wait()
    	d(description='zero').click.wait()
    	d(description='zero').click.wait()
    	d(description='one').click.wait()
    	d(description='zero').click.wait()
    	d(description='dial').click.wait()
        #step4
    	assert d(textContains='0:').wait.exists(timeout=10000), 'Call failed'
        time.sleep(10)
        #step5
    	d(description='End').click.wait()
    	assert d(description='Phone').wait.exists(), 'Call end failed'

if __name__ =='__main__':  
    unittest.main()