from uiautomator import device as d

import unittest, os, time

PACKAGE_NAME = 'com.google.android.music'
ACTIVITY_NAME = 'com.android.music.activitymanagement.TopLevelActivity'

class MusicTest(unittest.TestCase):
    def setUp(self):
        super(MusicTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(MusicTest, self).tearDown()

    def testOpenCloseMusicPlayer(self):
        """
        Summary:testOpenCloseMusicPlayer: Open/close the music player.
        Steps:1. Open Music app
              2. Exit Music app
        """ 
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Listen Now').wait.exists(timeout = 5000), 'Music player launch failed'


    def testOpenMusicPlayer(self):
        """
        Summary:testOpenMusicPlayer: Open music player.
        Steps: 1. Open music app
               2. Touch All tab
               3. Play a music file
               4. Back to home screen, run music on background
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Listen Now').wait.exists(), 'Music player launch failed'

        #step2
        d.swipe(0,400,400,400,steps=10)
        assert d(text = 'Playlists').wait.exists(), 'Option bar launch failed'

        d(text = 'Playlists').click.wait()
        assert d(text = 'Last added').wait.exists(), 'Playlists launch failed'

        #step3
        d(text = 'Last added').click.wait()
        d.click(120,400)
        assert d(description = 'Pause').wait.exists(), 'Music play failed'


    def testPlayMusicFile(self):
        """
        Summary:testPlayMusicFile: Play the music one by one till 50 cycles.
        Steps:1. Open Music app in background
              2. Touch Next button
              3. Touch HOME to run music on background
              4. Repeat Step 1,2,3 for 50 cycles
        """ 
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Listen Now').wait.exists(), 'Music player launch failed'
        assert d(description = 'Pause').wait.exists(), 'No music is palying' 

        d.click(130,900)

        #step2
        assert d(description = 'Next').wait.exists()
        d(description = 'Next').click.wait()


    def testCloseMusicPlayer(self):
        """
        Summary:testCloseMusicPlayer: Close music player.
        Steps:1. Open Music app
              2. Touch Next button
              3. Touch Pause button
              4. Exit Music app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(text = 'Listen Now').wait.exists(), 'Music player launch failed'
        assert d(description = 'Pause').wait.exists(), 'No music is palying' 

        d.click(130,900)

        #step2
        assert d(description = 'Next').wait.exists()
        d(description = 'Next').click.wait()

        #step3
        d(description = 'Pause').click.wait()
        assert d(description = 'Play').wait.exists(), 'Music pause failed'
        print('case4 finish')


if __name__ == '__main__':  
    unittest.main()

