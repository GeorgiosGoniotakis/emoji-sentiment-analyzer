import unittest

from source.data.EmojiLoader import EmojiLoader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_loader(self):
        loader = EmojiLoader(None)
        data = loader.load()
        self.assertNotEqual(None, data)


if __name__ == '__main__':
    unittest.main()
