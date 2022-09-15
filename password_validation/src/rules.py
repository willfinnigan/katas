from typing import Callable

Rule = Callable[[str], bool]

def has_characters(password):
    return password != ''

# use a closure to handle additional argument
def create_has_more_than_n_chars_rule(n):
    def has_more_than_or_equal_n_chars(password):
        return len(password) >= n
    return has_more_than_or_equal_n_chars

def has_a_capital(password):
    for l in password:
        if l.isupper():
            return True
    return False

def has_a_lower(password):
    for l in password:
        if l.islower():
            return True
    return False

def has_a_number(password):
    return any(i.isdigit() for i in password)

def has_a_underscore(password):
    return '_' in password