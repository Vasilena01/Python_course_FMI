import unittest
from Homework6 import *

class TestSanta(unittest.TestCase):
    def setUp(self):
        self.santa = Santa()
        self.goshko = BulgarianKid()
        self.toshko = BulgarianKid()
        self.chen = ChineseKid()

    def test_first_Xmas(self):
        self.santa(self.goshko, "'gun'")
        self.santa @ f"'gun'\n{id(self.toshko)}"

        try:
            self.goshko.be_naughty()
        except RuntimeError:
            pass

        self.santa.xmas()

        self.assertIn(self.goshko, self.santa.naughty_kids)
        self.assertEqual(self.santa.gifts[self.goshko], "coal")
        self.assertEqual(self.santa.gifts[self.toshko], "gun")
        self.assertEqual(self.santa.gifts[self.chen], "gun")

    def test_no_new_wishes_second_Xmas(self):
        self.santa.xmas()
            
        self.assertEqual(self.santa.gifts[self.goshko], "")
        self.assertEqual(self.santa.gifts[self.toshko], "")
        self.assertEqual(self.santa.gifts[self.chen], "")

    def test_no_new_wishes_third_Xmas(self):
        self.santa.xmas()

        self.assertEqual(self.santa.gifts[self.goshko], "")
        self.assertEqual(self.santa.gifts[self.toshko], "")
        self.assertEqual(self.santa.gifts[self.chen], "")
        
    def test_no_new_wishes_fourth_Xmas(self):
        self.santa.xmas()

        self.assertEqual(self.santa.gifts[self.goshko], "")
        self.assertEqual(self.santa.gifts[self.toshko], "")
        self.assertEqual(self.santa.gifts[self.chen], "")

    def test_fifth_Xmas_with_new_kid(self):
        gencho = BulgarianKid()
        self.santa(gencho, "'whistle'")

        self.santa.xmas()

        self.assertEqual(self.santa.gifts[self.goshko], "whistle")
        self.assertEqual(self.santa.gifts[self.toshko], "whistle")
        self.assertEqual(self.santa.gifts[self.chen], "whistle")
        self.assertEqual(self.santa.gifts[gencho], "whistle")
        
    def test_sixth_Xmas_with_another_new_kid(self):
        gencho = BulgarianKid()
        self.santa(gencho, "'whistle'")
        self.santa.xmas()

        kircho = BulgarianKid()
        self.santa(kircho, "'whistle'")
        self.santa.xmas()
            
        self.assertEqual(self.santa.gifts[kircho], "whistle")
        self.assertEqual(self.santa.gifts[gencho], "whistle")
        self.assertEqual(self.santa.gifts[self.goshko], "")
        self.assertEqual(self.santa.gifts[self.toshko], "")
        self.assertEqual(self.santa.gifts[self.chen], "")


if __name__ == "__main__":
    unittest.main()