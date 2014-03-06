from uiautomator import device as d

import unittest, os, random

PACKAGE_NAME = 'com.android.contacts'
ACTIVITY_NAME = PACKAGE_NAME + '.activities.PeopleActivity'

CONTACT_NAME = 'test'
random_name = str(random.randint(0,1000))
PHONE_NUMBER = '10010'
GET_CONTACT_COUNT_COMMAND = 'adb shell sqlite3 /data/data/com.android.providers.contacts/databases/contacts2.db "select count(*) from view_v1_people"'


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

    def testAddContact(self):
        """
        Summary:testAddContact: Add a contact.
        Steps:
          1. Open Contacts app
          2. Touch Add button
          3. Input contact name and number
          4. Touch Done button
          5. Exit Contacts app
        """
        result1 = os.popen(GET_CONTACT_COUNT_COMMAND).read()
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'All contacts').wait.exists(), 'Contact launch failed'
        d(description = 'All contacts').click.wait()

        #step2
        d(description = 'Add Contact').click.wait()

        #step3
        d(text = "Name").set_text(CONTACT_NAME + random_name)
        d(text = "Phone", className = 'android.widget.EditText').set_text(PHONE_NUMBER)

        #step4
        d(text = 'Done').click.wait()

        result2 = os.popen(GET_CONTACT_COUNT_COMMAND).read()

        if int(result2) == int(result1) + 1:
            assert True
        else:
            assert False, 'Contact add failed'

    def testDeleteContact(self):
        """
        Summary:testDeleteContact: Delete a contact.
        Precondition: 
              1. Contacts exist
              
        Steps:1. Open Contacts app
              2. Touch a contact item to view the contact
              3. Delete the contact
              4. Exit Contacts app
        """
        result1 = os.popen(GET_CONTACT_COUNT_COMMAND).read()
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'All contacts').wait.exists(), 'Contact launch failed'
        d(description = 'All contacts').click.wait()

        #step2
        d(textContains = 'test').click.wait()

        #step3
        d.press('menu')
        d(text = 'Delete').click.wait()
        d(text = 'OK').click.wait()

        result2 = os.popen(GET_CONTACT_COUNT_COMMAND).read()

        if int(result2) == int(result1) - 1:
            assert True
        else:
            assert False, 'Contact delete failed'


if __name__ == '__main__':  
    unittest.main()