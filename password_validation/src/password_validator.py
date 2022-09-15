from password_validation.src.rules import Rule


class PasswordValidator():

    def __init__(self, allowed_fails=0):
        self.rules = []
        self.allowed_fails = allowed_fails

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def validate(self, password: str):
        evaluated_rules = [rule(password) for rule in self.rules]
        if evaluated_rules.count(False) > self.allowed_fails:
            return False
        return True





