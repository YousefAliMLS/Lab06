import unittest
import test


class TestTask(unittest.TestCase):
    def setUp(self):
        self.t = test.Task()

    def test_add(self):
        self.assertEqual(self.t.add(5, 10), 15)

    def test_subtract(self):
        self.assertEqual(self.t.subtract(10, 5), 5)

    def test_print(self):
        # test.print(123) should return "yes"
        self.assertEqual(self.t.print(123), "yes")
        # for other values, method returns None
        self.assertIsNone(self.t.print(0))


if __name__ == "__main__":
    unittest.main()
