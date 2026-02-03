import unittest
from text_utils import count_lines, count_words, most_common_word


class TestTextUtils(unittest.TestCase):
    def test_count_lines(self):
        text_1 = "Hello World\nThis is a test.\nAnother line."
        self.assertEqual(count_lines(text_1), 3)
        text_2 = "Hello"
        self.assertEqual(count_lines(text_2), 1)
        text_3 = ""
        self.assertEqual(count_lines(text_3), 0)

    def test_count_words(self):
        text_1 = "Hello, world! Hello everyone."
        self.assertEqual(count_words(text_1), 4)
        text_2 = " "
        self.assertEqual(count_words(text_2), 0)
        text_3 = "can't can't"
        self.assertEqual(count_words(text_3), 2)

    def test_most_common_word(self):
        text = "apple banana apple orange banana apple"
        self.assertEqual(most_common_word(text), "apple")

    def test_most_common_word_empty(self):
        text = ""
        self.assertEqual(most_common_word(text), "")


if __name__ == '__main__':
    unittest.main()
