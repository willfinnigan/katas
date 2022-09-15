from password_validation.src.rules import Rule


class PasswordValidator():

    def __init__(self, allowed_fails=0):
        self.rules = []
        self.allowed_fails = allowed_fails

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def number_of_failed_rules(self, password: str):
        """Returns the number of failed rules"""
        evaluated_rules = self.evaluate_rules(password)
        return evaluated_rules.count(False)

    def evaluate_rules(self, password: str):
        """Returns a list of True/False for rules which pass/fail"""
        return [rule(password) for rule in self.rules]

    def validate(self, password: str):
        """Returns True if password passes validation"""
        if self.number_of_failed_rules(password) > self.allowed_fails:
            return False
        return True





