import unittest
import main as m

class MyTests(unittest.TestCase):

    def test_add1(self):
        res = m.add(5,6)
        self.assertEqual(res, 11)

    def test_add2(self):
        res = m.add(-5,6)
        self.assertEqual(res, 1)

    def test_add3(self):
        res = m.add(-5,-6)
        self.assertEqual(res, -11, "error when result is negative")

def main():
    unittest.main()


if __name__ == "__main__":
    main()
