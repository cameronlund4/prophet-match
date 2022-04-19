import unittest

from phrase_match import is_phrase_match


class TestPhraseMatch(unittest.TestCase):
    def test_basic(self):
        """
        basic match
        """
        self.assertTrue(is_phrase_match("ceo", "ceo"))

    def test_basic_fail(self):
        """
        basic negative match
        """
        self.assertFalse(is_phrase_match("ceo", "cfo"))

    def test_empty_body(self):
        """
        ceo is not in empty
        """
        self.assertFalse(is_phrase_match("ceo", ""))

    def test_empty_search(self):
        """
        empty is in everything (this case is not super important, if this
        is the only one failing, dump it)
        """
        self.assertTrue(is_phrase_match("", "ceo"))

    def test_basic_case_insensitivity(self):
        """
        case insensitivity, match into body
        """
        self.assertTrue(is_phrase_match("cEo", "ceo"))

    def test_basic_case_insensitivity_2(self):
        """
        case insensitivity, body into match
        """
        self.assertTrue(is_phrase_match("ceo", "cEo"))

    def test_start_of_sentence(self):
        """
        match at beginning
        """
        self.assertTrue(is_phrase_match("ceo", "cEo people are really cool"))

    def test_end_of_sentence(self):
        """
        match at end
        """
        self.assertTrue(is_phrase_match("ceo", "I am the cEo"))

    def test_middle_of_sentence(self):
        """
        match in middle
        """
        self.assertTrue(is_phrase_match("ceo", "I think CeO is Super cool!"))

    def test_weird_spacing(self):
        """
        match in middle
        """
        self.assertTrue(is_phrase_match("ceo", "I think\tCeO\tis Super cool!"))

    def test_multiple(self):
        """
        match with multiple
        """
        self.assertTrue(
            is_phrase_match("ceo", ("I think CeO is Super cool! ceo rad, ceo sick"))
        )

    def test_in_word(self):
        """
        test in word, but not real match
        """
        self.assertFalse(is_phrase_match("cOo", ("coordinator")))

    def test_in_word_case_match(self):
        """
        test in word, case match
        """
        self.assertFalse(is_phrase_match("COO", ("COOrdinator")))

    def test_in_word_sentence_beginning(self):
        """
        test in word at beginning of sentence
        """
        self.assertFalse(
            is_phrase_match("coo", ("coordinators are really cool people"))
        )

    def test_in_word_sentence_end(self):
        """
        test in word at end of sentence
        """
        self.assertFalse(is_phrase_match("coo", ("I want to be a coordinator")))

    def test_in_word_and_sentence(self):
        """
        test in word, but also in the sentence, so good
        """
        self.assertTrue(
            is_phrase_match(
                "coo", ("I want to be a coordinator, but currently I am a coo")
            )
        )

    # TODO Harder test to pass, uncomment when others done
    # def test_ignore_nonalpha(self):
    #     """
    #     we don't want punctuation to screw us up
    #     """
    #     self.assertTrue(is_phrase_match("coo", "I am the coo's secretary"))
    #     self.assertTrue(is_phrase_match("coo", "I am the coo."))
    #     self.assertTrue(is_phrase_match("coo", "I am the coo, and the cfo"))
    #     self.assertTrue(
    #         is_phrase_match("coo", "I am the coo: chief operations officer")
    #     )
    #     self.assertTrue(is_phrase_match("coo", "I am the coo!"))
    #     self.assertTrue(is_phrase_match("coo", "I am the coo73"))


if __name__ == "__main__":
    unittest.main()
