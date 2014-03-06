from uiautomator import device as d

import unittest, os, time

PACKAGE_NAME = 'com.android.gallery3d'
ACTIVITY_NAME = 'com.android.camera.CameraLauncher'

QUERY_PICTURE_COUNT_COMMANDS = 'adb shell ls /mnt/sdcard/DCIM/Camera/  | grep IMG | wc -l'
QUERY_VIDEO_COUNT_COMMANDS = 'adb shell ls /mnt/sdcard/DCIM/Camera/  | grep 3gp | wc -l'


class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest, self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME

    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('home')
        super(CameraTest, self).tearDown()

    def testTakePicture(self):
        """
        Summary:testTakePicture: Take a picture.
        Steps:1. Open Camera app
              2. Capture a picture
              3. Exit Camera app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Shutter button').wait.exists(), 'Camera launch failed'

        result1 = os.popen(QUERY_PICTURE_COUNT_COMMANDS).read()

        #step2
        d(description = 'Shutter button').click.wait(timeout=3000)

        #step3
        result2 = os.popen(QUERY_PICTURE_COUNT_COMMANDS).read()

        if int(result2) == int(result1) + 1:
            assert True
        else:
            assert False, 'Capture failed'

    def testOpenPicture(self):
        """
        Summary:testCapturePictureAndDelete: Take a picture, then view and delete the picture.
        Steps:1. Open Camera app
              2. Touch thumbnail to view the picture
              3. Exit Camera app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Shutter button').wait.exists(), 'Camera launch failed'

        #Step2
        d.swipe(520,500,120,500,steps = 10)
        time.sleep(2)
        d.click(274,482)
        d.press('menu')
        assert d(text = 'Delete').wait.exists()

    def testDeletePicture(self):
        """
        Summary:testCapturePictureAndDelete: Take a picture, then view and delete the picture.
        Steps:1. Open Camera app
              2. Touch thumbnail to view the picture
              3. Touch setting menu
              4. Touch Delete button to delete the picture
              5. Exit Camera app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Shutter button').wait.exists(), 'Camera launch failed'

        result1 = os.popen(QUERY_PICTURE_COUNT_COMMANDS).read()

        #step2
        d.swipe(520,500,120,500,steps = 10)
        time.sleep(2)
        d.click(274,482)

        #step3
        d.press('menu')
        assert d(text = 'Delete').wait.exists()

        #step4
        d(text = 'Delete').click.wait()
        d(text = 'OK').click.wait(timeout = 2000)

        result2 = os.popen(QUERY_PICTURE_COUNT_COMMANDS).read()
        if int(result2) == int(result1) - 1:
            assert True
        else:
            assert False, 'Picture delete failed'

    def testRecordVideo(self):
        """
        Summary:testRecordVideoAndDelete: Record a video, then play and delete the video.
        Steps:1. Open Camera app
              2. Record a video 30s
              3. Exit Camera app
        """
        #step1
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Shutter button').wait.exists(), 'Camera launch failed'

        result1 = os.popen(QUERY_VIDEO_COUNT_COMMANDS).read()

        d(description = 'Camera, video, or panorama selector').click.wait()
        d(description = 'Switch to video').click.wait()
        assert d(description = 'Shutter button').wait.exists(), 'Video Camera launch failed'

        #step2
        d(description = 'Shutter button').click.wait(timeout=30000)
        d(description = 'Shutter button').click.wait(timeout=5000)

        result2=os.popen(QUERY_VIDEO_COUNT_COMMANDS).read()
        if int(result2) == int(result1) + 1:
            assert True
        else:
            assert False, 'Video record failed'

    def testPlayVideo(self):
        """
        Summary:testRecordVideoAndDelete: Record a video, then play and delete the video.
        Steps:1. Open Camera app
              2. Record a video
              3. Touch thumbnail to view the video
              4. Tocuh screen center to play the video
              5. Exit Camera app
        """
        #step1,2
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Shutter button').wait.exists(), 'Camera launch failed'
        d(description = 'Camera, video, or panorama selector').click.wait()
        d(description = 'Switch to video').click.wait()
        assert d(description = 'Shutter button').wait.exists(), 'Video Camera launch failed'

        #step3
        d.swipe(520,500,120,500,steps = 10)
        time.sleep(2)
        d.click(274,482)
        d.press('menu')
        assert d(text = 'Delete').wait.exists()

        #step4
        d.press('back')
        d.click(274,482)
        time.sleep(10)
        d.click(274,482)
        assert d(index = 2, className = 'android.view.View').wait.exists(), 'Video play failed'

    def testDeleteVideo(self):
        """
        Summary:testRecordVideoAndDelete: Record a video, then play and delete the video.
        Steps:1. Open Camera app
              2. Record a video
              3. Touch thumbnail to view the video
              4. Touch Delete button to delete the video
              5. Exit Camera app
        """
        result1=os.popen(QUERY_VIDEO_COUNT_COMMANDS).read()

        #step1,2
        os.system('adb shell am start ' + self.runComponent)
        assert d(description = 'Shutter button').wait.exists(), 'Camera launch failed'
        d(description = 'Camera, video, or panorama selector').click.wait()
        d(description = 'Switch to video').click.wait()
        assert d(description = 'Shutter button').wait.exists(), 'Video Camera launch failed'

        #step3
        d.swipe(520,500,120,500,steps = 10)
        time.sleep(2)
        d.click(274,482)

        #step4
        d.press('menu')
        assert d(text = 'Delete').wait.exists()
        d(text = 'Delete').click.wait()
        d(text = 'OK').click.wait(timeout = 2000)

        result2 = os.popen(QUERY_VIDEO_COUNT_COMMANDS).read()

        if int(result2) == int(result1) - 1:
            assert True
        else:
            assert False, 'Video record failed'


if __name__ == '__main__':  
    unittest.main()