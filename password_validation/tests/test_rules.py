from password_validation.src.rules import has_characters, has_more_than_or_equal_n_chars, has_a_capital, has_a_lower, \
    has_a_number, has_a_underscore

def test_empty_password_fails_has_characters():
    assert has_characters('') is False

def test_password_passes_has_characters():
    assert has_characters('not_empty') is True

def test_password_with_less_than_8_chars_fails():
    assert has_more_than_or_equal_n_chars('1234', 8) is False

def test_password_with_8_chars_passes():
    assert has_more_than_or_equal_n_chars('12345678', 8) is True

def test_password_with_a_capital_passes():
    assert has_a_capital('Hello') is True

def test_password_with_no_capital_letter_fails():
    assert has_a_capital('hello') is False

def test_password_with_a_lower_passes():
    assert has_a_lower('Hello') is True

def test_password_only_captical_fails():
    assert has_a_lower('HELLO') is False

def test_password_with_no_number_fails():
    assert has_a_number('this is not a number') is False

def test_password_with_a_number_passes():
    assert has_a_number('Hello1') is True

def test_password_with_underscore_passes():
    assert has_a_uenderscore('I_have_underscores') is True

def test_password_without_underscore_fails():
    assert has_a_underscore('I have no underscores') is False
