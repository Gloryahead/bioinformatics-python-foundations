import unittest
from text_utils import count_lines, count_words, most_common_word


class TestTextUtils(unittest.TestCase):

    def test_count_lines(self):
        cases = [
            ("Hello World\nThis is a test.\nAnother line.", 3),
            ("Hello", 1),
            ("", 0),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_lines(text), expected)

    def test_count_words(self):
        cases = [
            ("Hello, world! Hello everyone.", 4),
            ("   \n\t  ", 0),
            ("can't can't", 2),
            ("Hi, hi. HI!", 3),  # punctuation + case-insensitive normalization
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_words(text), expected)

    def test_most_common_word(self):
        cases = [
            ("apple banana apple orange banana apple", "apple"),
            ("", ""),
            ("Hi, hi. HI!", "hi"),
            ("a a b", "a"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(most_common_word(text), expected)


if __name__ == '__main__':
    unittest.main()
