"""Plain-assert tests, so they run without any test dependency."""

from app import word_count


def test_counts_words():
    assert word_count("one two three") == 3


def test_ignores_extra_whitespace():
    assert word_count("  one   two  ") == 2


if __name__ == "__main__":
    test_counts_words()
    test_ignores_extra_whitespace()
    print("ok")
