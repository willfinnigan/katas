import pytest
from password_validation.src.password_validator import PasswordValidator
from password_validation.src.rules import (has_characters,
                                           has_more_than_or_equal_n_chars,
                                           has_a_number,
                                           has_a_underscore,
                                           has_a_lower,
                                           has_a_capital)

test_cases = [('Password1_', True),   # passes all conditions
              ('AlsoPassesAll2_', True),   # passes all conditions
              ('', False),   # empty string fails
              ("Pass1_", False),  # too short fails
              ('password1_', False),  # no caps fails
              ("PASSWORD1_", False),  # all caps fails
              ("Password_", False),  # no number fails
              ("Password1", False),  # no underscore fails
              ]

@pytest.mark.parametrize('password, expected', test_cases)
def test_validator(password, expected):
    validator = PasswordValidator()
    validator.add_rule(has_characters)
    validator.add_rule(has_more_than_or_equal_n_chars, 8)
    validator.add_rule(has_a_capital)
    validator.add_rule(has_a_lower)
    validator.add_rule(has_a_number)
    validator.add_rule(has_a_underscore)
    assert validator.validate(password) is expected


# Validation 2:
test_cases_2 = [('Password1', True),   # passes all conditions
                ('AlsoPassesAll2', True),   # passes all conditions
                ("Pass1", False),  # too short fails
                ('password1', False),  # no caps fails
                ("PASSWORD1", False),  # all caps fails
                ]

@pytest.mark.parametrize('password, expected', test_cases_2)
def test_validator_two(password, expected):
    validator = PasswordValidator()
    validator.add_rule(has_more_than_or_equal_n_chars, 6)
    validator.add_rule(has_a_capital)
    validator.add_rule(has_a_lower)
    validator.add_rule(has_a_number)
    assert validator.validate(password) is expected


# Validation 3:
test_cases_3 = [('Password_with_more_than_sixteen', True),   # passes all conditions
                ('AlsoPasses_Because_Very_Long', True),   # passes all conditions
                ("Pass_", False),  # too short fails
                ('Password with more than sixteen', False),  # no underscore fails
                ('password_with_more_than_sixteen', False),  # all lower case fails
                ]

@pytest.mark.parametrize('password, expected', test_cases_3)
def test_validator_three(password, expected):
    validator = PasswordValidator()
    validator.add_rule(has_more_than_or_equal_n_chars, 16)
    validator.add_rule(has_a_capital)
    validator.add_rule(has_a_underscore)
    assert validator.validate(password) is expected


# Validation 4:
test_cases_4 = [('Password1_', True),   # passes all conditions
                ('AlsoPasses2_', True),   # passes all conditions
                ("Pass1_", True),  # passes because fails only 1 (too short)
                ('Password_', True),  # passes because fails only 1 (no number)
                ("Pass1", False),  # fails because too short AND no number
                ("password1", False),  # fails because no caps AND no number
                ]

@pytest.mark.parametrize('password, expected', test_cases_4)
def test_validator_four(password, expected):
    validator = PasswordValidator(allowed_fails=1)
    validator.add_rule(has_more_than_or_equal_n_chars, 8)
    validator.add_rule(has_a_capital)
    validator.add_rule(has_a_number)
    validator.add_rule(has_a_underscore)
    assert validator.validate(password) is expected



