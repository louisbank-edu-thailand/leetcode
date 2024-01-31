import leetcode


def test_is_palindrome_true():
    assert leetcode.is_palindrome("baab") == True


def test_is_palindrome_false():
    assert leetcode.is_palindrome("hello") == False


def test_is_palindrome_empty():
    assert leetcode.is_palindrome("") == True
