
class PasswordValidator():

    def __init__(self, allowed_fails=0):
        self.rules = []
        self.allowed_fails = allowed_fails

    def add_rule(self, rule, *args):
        self.rules.append((rule, args))

    def number_of_failed_rules(self, password):
        """Returns the number of failed rules"""
        evaluated_rules = self.evaluate_rules(password)
        return evaluated_rules.count(False)

    def evaluate_rules(self, password):
        """Returns a list of True/False for rules which pass/fail"""
        return [rule(password, *args) for (rule, args) in self.rules]

    def validate(self, password):
        """Returns True if password passes validation"""
        if self.number_of_failed_rules(password) > self.allowed_fails:
            return False
        return True





