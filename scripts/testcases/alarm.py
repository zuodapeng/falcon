#!/usr/bin/env python

from uiautomator import device as d

import unittest, os


PACKAGE_NAME = 'com.google.android.deskclock'
ACTIVITY_NAME = 'com.android.deskclock.DeskClock'

QUERY_ALARM_COUNT_COMMANDS = 'adb shell sqlite3 /data/data/com.google.android.deskclock/databases/alarms.db "select count(*) from alarm"'

class AlarmTest(unittest.TestCase):
    def setUp(self):
        super(AlarmTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        d.wakeup()
        d.press('home')

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('home')
        super(AlarmTest, self).tearDown()

    def testAlarmAdd(self):
        '''
        Summary:testAlarmAdd: Add an alarm.
        Steps:
                1.Launch alarm and check launch successfully
                2.Get alarm number
                3.Verify alarm is exist or inexistence
                4.If exist alarm, delete it
                5.Add alarm
        '''
        #step1
        os.system('adb shell am start ' + self.runComponent)
    	assert d(description = 'Alarms').wait.exists(), 'Clock launch failed'

    	d(description = 'Alarms').click.wait()
    	assert d(text = 'Alarms').wait.exists(), 'Alarm launch failed'

        #step2
    	result1 = os.popen(QUERY_ALARM_COUNT_COMMANDS)

    	#step3,4
    	for i in range(0,int(result1.read())):
    		d.swipe(45,158,500,158,steps=10)
    		assert d(text = 'Alarm deleted.'), 'Alarm delete failed'

    	#step5
    	d(description = 'Add alarm').click.wait()
    	d(text = 'Cancel').click.wait()

    	assert d(text = '12').wait.exists(), 'Alarm create failed'


    def testAlarmDelete(self):
        """
        Summary:testAlarmDelete: Delete an alarm.
        Steps:
                1.Launch alarm and check launch successfully
                2.Verify alarm is with or without
                3.Exist is pass, inexistence is add an alarm
                4.Delete an alarm
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Alarms').wait.exists(), 'Clock launch failed'

        d(description = 'Alarms').click.wait()
        assert d(text = 'Alarms').wait.exists(), 'Alarm launch failed'

        #step2,3
        result1 = os.popen(QUERY_ALARM_COUNT_COMMANDS)
        if int(result1.read()) == 0:
            d(description = 'Add alarm').click.wait()
            d(text = 'Cancel').click.wait()

        #step4
        d.swipe(45,158,500,158,steps = 10)
        assert d(text = 'Alarm deleted.'), 'Alarm delete failed'
        


if __name__ == '__main__':  
    unittest.main()