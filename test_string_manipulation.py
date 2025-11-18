import unittest
from string_manipulation import *

class TestStringFunctions(unittest.TestCase):

    # --- Easy ---

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("WORLD"), "WORLD")
        self.assertEqual(to_uppercase("PyThOn"), "PYTHON")
        self.assertEqual(to_uppercase("Hello 123!"), "HELLO 123!")
        self.assertEqual(to_uppercase(""), "")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("world"), "world")
        self.assertEqual(to_lowercase("PyThOn"), "python")
        self.assertEqual(to_lowercase("Hello 123!"), "hello 123!")
        self.assertEqual(to_lowercase(""), "")

    def test_count_char(self):
        self.assertEqual(count_char("hello", "l"), 2)
        self.assertEqual(count_char("Hello", "h"), 0)
        self.assertEqual(count_char("Hello", "H"), 1)
        self.assertEqual(count_char("world", "a"), 0)
        self.assertEqual(count_char("the quick brown fox", " "), 3)
        self.assertEqual(count_char("", "a"), 0)
        self.assertEqual(count_char("101010001", "1"), 4)

    # --- Medium ---

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("Python 3.8!"), "!8.3 nohtyP")
        self.assertEqual(reverse_string("the quick brown fox"), "xof nworb kciuq eht")

    def test_reverse_sentence(self):
        self.assertEqual(reverse_sentence("the car is fast"), "fast is car the")
        self.assertEqual(reverse_sentence("hello world"), "world hello")
        self.assertEqual(reverse_sentence(""), "")
        self.assertEqual(reverse_sentence("hello"), "hello")
        self.assertEqual(reverse_sentence("the   quick brown   fox"), "fox brown quick the")
        self.assertEqual(reverse_sentence("  leading and trailing  "), "trailing and leading")
        self.assertEqual(reverse_sentence("a man a plan a canal panama"), "panama canal a plan a man a")
        self.assertEqual(reverse_sentence("Was it a car or a cat I saw?"), "saw? I cat a or car a it Was")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("racecar"), True)
        self.assertEqual(is_palindrome("hello"), False)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("Madam"), True)
        self.assertEqual(is_palindrome("Noon"), True)
        self.assertEqual(is_palindrome("nurses run"), True)
        self.assertEqual(is_palindrome("taco cat"), True)
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(is_palindrome("Was it a car or a cat I saw?"), True)
        self.assertEqual(is_palindrome("Don't nod."), True)
        self.assertEqual(is_palindrome("abcdeba"), False)
        self.assertEqual(is_palindrome("12321"), True)
        self.assertEqual(is_palindrome("A1b2B1a"), True)
        self.assertEqual(is_palindrome("12345"), False)

    # --- Hard ---

    def test_is_anagram(self):
        self.assertEqual(is_anagram("listen", "silent"), True)
        self.assertEqual(is_anagram("triangle", "integral"), True)
        self.assertEqual(is_anagram("Listen", "Silent"), True)
        self.assertEqual(is_anagram("Dormitory", "dirty room"), True)
        self.assertEqual(is_anagram("Astronomer", "Moon starer"), True)
        self.assertEqual(is_anagram("The eyes", "They see"), True)
        self.assertEqual(is_anagram("hello", "billion"), False)
        self.assertEqual(is_anagram("apple", "apply"), False)
        self.assertEqual(is_anagram("aaa", "aa"), False)
        self.assertEqual(is_anagram("", ""), True)

    def test_format_date(self):
        self.assertEqual(format_date("13 november 2025"), "13/11/2025")
        self.assertEqual(format_date("2 january 2024"), "02/01/2024")
        self.assertEqual(format_date("28 february 1999"), "28/02/1999")
        self.assertEqual(format_date("31 december 2000"), "31/12/2000")
        self.assertEqual(format_date("1 january 2001"), "01/01/2001")
        self.assertEqual(format_date("5 may 1980"), "05/05/1980")
        self.assertEqual(format_date("10 March 2010"), "10/03/2010")
        self.assertEqual(format_date("20 AUGUST 1995"), "20/08/1995")
        self.assertEqual(format_date("15 aprIl 2021"), "15/04/2021")

if __name__ == "__main__":
    unittest.main()