def assert_equals(expected, actual, message: str):
    if expected != actual:
        raise AssertionError(message)


def check_substring(substring, string, message: str):
    if substring not in string:
        raise AssertionError(message)
