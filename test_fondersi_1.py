import unittest
import fondersi

file_name1 = "D:\Images\map99.jpg"
file_name2 = "\imags\img33.png"
file_name3 = "\imags\img33.mp3"
file_name4 = "\imags\img33.pngg"

class TestCheckImageExtension(unittest.TestCase):
    def test_check_image_extension(self):
        # test check image extensions
        self.assertEqual(fondersi.check_image_extension(file_name1), True)
        self.assertEqual(fondersi.check_image_extension(file_name2), True)
        self.assertEqual(fondersi.check_image_extension(file_name3), False)
        self.assertEqual(fondersi.check_image_extension(file_name4), False)
