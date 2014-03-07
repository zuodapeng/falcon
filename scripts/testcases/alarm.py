#!/usr/bin/env python

from uiautomator import device as d
import unittest, os, commands

#alarm package/activity name
PACKAGE_NAME = 'com.google.android.deskclock'
ACTIVITY_NAME = 'com.android.deskclock.DeskClock'

#get alarm count
QUERY_ALARM_COUNT_COMMANDS = 'adb shell sqlite3 /data/data/com.google.android.deskclock/databases/alarms.db "select count(*) from alarms"'

#for delete alarm
startX = 45
startY = 158
endX = 500
endY = 158

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
        #os.system('adb shell am start ' + self.runComponent)
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Alarms').wait.exists(), 'Clock launch failed'

        d(description = 'Alarms').click.wait()
        assert d(text = 'Alarms').wait.exists(), 'Alarm launch failed'

        #step2
        #BEFORE_DELETE = os.popen(QUERY_ALARM_COUNT_COMMANDS)
        BEFORE_DELETE = commands.getoutput(QUERY_ALARM_COUNT_COMMANDS)

        #step3,4
        for i in range(0, int(BEFORE_DELETE)):
            d.swipe(startX, startY, endX, endY, steps = 10)
            assert d(text = 'Alarm deleted.'), 'Alarm delete failed'
            
        #AFTER_DELETE = os.popen(QUERY_ALARM_COUNT_COMMANDS)
        AFTER_DELETE = commands.getoutput(QUERY_ALARM_COUNT_COMMANDS)
        assert int(AFTER_DELETE) == 0, 'Still exist alarm'


        #step5
        d(description = 'Add alarm').click.wait()
        d(text = 'Cancel').click.wait()

        assert d(text = ':00').wait.exists(), 'Alarm create failed'



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
        commands.getoutput('adb shell am start ' + self.runComponent)
        assert d(description = 'Alarms').wait.exists(), 'Clock launch failed'

        d(description = 'Alarms').click.wait()
        assert d(text = 'Alarms').wait.exists(), 'Alarm launch failed'

        #step2,3
        ALARM_COUNT = commands.getoutput(QUERY_ALARM_COUNT_COMMANDS)
        if int(ALARM_COUNT) == 0:
            d(description = 'Add alarm').click.wait()
            d(text = 'Cancel').click.wait()

        #step4
        d.swipe(startX, startY, endX, endY, steps = 10)
        assert d(text = 'Alarm deleted.'), 'Alarm delete failed'
        


if __name__ == '__main__':  
    unittest.main()