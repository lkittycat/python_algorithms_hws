import unittest

from algo import group_anagrams


class TestAnagrams(unittest.TestCase):
    def check_groups(self, words, expected):
        result = group_anagrams(words)
        # Порядок групп и слов не важен, но повторы должны сохраниться.
        self.assertCountEqual(
            [tuple(sorted(group)) for group in result],
            [tuple(sorted(group)) for group in expected],
        )

    def test_example(self):
        self.check_groups(
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )

    def test_empty_list(self):
        self.check_groups([], [])

    def test_one_word(self):
        self.check_groups(["cat"], [["cat"]])

    def test_empty_word(self):
        self.check_groups([""], [[""]])

    def test_empty_words_with_other_words(self):
        self.check_groups(["", "ab", "", "ba"], [["", ""], ["ab", "ba"]])

    def test_all_in_one_group(self):
        self.check_groups(["abc", "bca", "cab", "cba"], [["abc", "bca", "cab", "cba"]])

    def test_no_anagrams(self):
        self.check_groups(["cat", "dog", "sun"], [["cat"], ["dog"], ["sun"]])

    def test_repeated_words(self):
        self.check_groups(["eat", "eat", "tea", "bat", "bat"], [["eat", "eat", "tea"], ["bat", "bat"]])

    def test_letter_counts_matter(self):
        self.check_groups(["ab", "aab", "aba", "abb", "bba"], [["ab"], ["aab", "aba"], ["abb", "bba"]])

    def test_one_letter_words(self):
        self.check_groups(["a", "b", "a", "c"], [["a", "a"], ["b"], ["c"]])

    def test_capital_letters(self):
        self.check_groups(["Ab", "bA", "ab", "ba"], [["Ab", "bA"], ["ab", "ba"]])

    def test_russian_words(self):
        self.check_groups(["кот", "ток", "сон", "нос"], [["кот", "ток"], ["сон", "нос"]])

    def test_input_doesnt_change(self):
        words = ["tea", "bat", "eat"]
        self.check_groups(words, [["tea", "eat"], ["bat"]])
        self.assertEqual(words, ["tea", "bat", "eat"])

    def test_many_words(self):
        self.check_groups(["ab", "ba", "cat"] * 1000, [["ab", "ba"] * 1000, ["cat"] * 1000])


if __name__ == "__main__":
    unittest.main()
