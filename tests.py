import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        password = "charis7"
        self.assertFalse(check_pwd(password))

    def test2(self):
        password = "eightchr"
        self.assertTrue(check_pwd(password))

    def test3(self):
        password = "thisistwentycharac20"
        self.assertTrue(check_pwd(password))


if __name__ == '__main__':
    unittest.main()