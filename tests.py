import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        password = "charis7"
        self.assertFalse(check_pwd(password))


if __name__ == '__main__':
    unittest.main()