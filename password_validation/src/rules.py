
def has_characters(password):
    return password != ''

def has_more_than_or_equal_n_chars(password, n):
    return len(password) >= n

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