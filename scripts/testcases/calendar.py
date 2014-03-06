from uiautomator import device as d

import unittest, os, random, time

PACKAGE_NAME = 'com.google.android.calendar'
ACTIVITY_NAME = 'com.android.calendar.AllInOneActivity'

QUERY_EVENTS_COUNT_COMMANDS = 'adb shell sqlite3 /data/data/com.android.providers.calendar/databases/calendar.db "select count(*) from Events"'

EVENT_NAME = 'AddEvent'

DAY_NUMBER = random.randint(0, 27)

class CalendarTest(unittest.TestCase):
	
	def setUp(self):
		super(CalendarTest, self).setUp()
		self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        d.wakeup()
        d.press('home')

	def tearDown(self):
		d.press('back')
		d.press('back')
		d.press('home')
		super(CalendarTest, self).tearDown()

	def testCalendarAddEvent(self):
		"""
        Summary:testCalendarAddEvent: Add an event in calendar.
        Steps:
                1.Launch Calendar and check launch successfully
                2.Get events number
                3.Enter add event interface
                4.Input event name
                5.Set event time and add event
                6.Verify event is add successfully
		"""
        #step1
		os.system('adb shell am start '+self.runComponent)
		d.press('menu')
		assert d(text='New event').wait.exists(), 'Calendar launch failed'

        #step2
		result1=os.popen(QUERY_EVENTS_COUNT_COMMANDS).read()
		print(result1)

        #step3
		d(text='New event').click.wait()
		assert d(text='Done').wait.exists(), 'Calendar create failed'

        #step4
		d(text='Event name').set_text(EVENT_NAME)

        #step5
		d.click(73,415)
		d(index=DAY_NUMBER, className='com.android.datetimepicker.date.SimpleMonthAdapter$CalendarDay').click.wait()
		d.click(275,875)
		#d(text='Done', className='android.widget.Button').wait.click()
		time.sleep(1)
		d.click(400,75)
		#d(text='Done', className='android.widget.TextView').wait.click()
		time.sleep(2)

        #step6
		result2=os.popen(QUERY_EVENTS_COUNT_COMMANDS).read()
		print(result2)

		if int(result2) == int(result1) + 1:
			assert True
		else:
			assert False, 'Calendar add failed'

	def testCalendarDeleteEvent(self):
		"""
        Summary:testCalendarAddEvent: Add an event in calendar.
        Steps:
                1.Launch Calendar and check launch successfully
                2.Get events number
                3.Enter agenda interface
                4.Enter envent
                5.Touch delete icon
                6.Verify event number is delete successfully
		"""
        #step1
		os.system('adb shell am start '+self.runComponent)
		d.press('menu')
		assert d(text='New event').wait.exists(), 'Calendar launch failed'

        #step2
		result1=os.popen(QUERY_EVENTS_COUNT_COMMANDS).read()
		print(result1)

		if int(result1) == 0:
			d(text='New event').click.wait()
			d(text='Event name').set_text(EVENT_NAME)
			d.click(73,415)
			d(index=DAY_NUMBER, className='com.android.datetimepicker.date.SimpleMonthAdapter$CalendarDay').click.wait()
			d.click(275,875)
			time.sleep(1)
			d.click(400,75)
			time.sleep(2)
		else:
			d.press('back')

		result2=os.popen(QUERY_EVENTS_COUNT_COMMANDS).read()
		print(result2)

        #step3
		d(index=0, className='android.widget.Spinner').click.wait()
		d(text='Agenda').click.wait()

        #step4
		d(text='AddEvent').click.wait()

        #step5
		d(description='Delete').click.wait()
		d(text='OK').click.wait()

        #step6
		result3=os.popen(QUERY_EVENTS_COUNT_COMMANDS).read()
		print(result3)

		if int(result3) == int(result2) - 1:
			assert True
		else:
			assert False, 'Calendar delete failed'


if __name__ =='__main__':  
	unittest.main()