
class PasswordValidator():

    def __init__(self, allowed_fails=0):
        self.rules = []
        self.allowed_fails = allowed_fails

    def add_rule(self, rule, *args):
        self.rules.append((rule, args))

    def _number_of_failed_rules(self, password):
        count = 0
        for rule, args in self.rules:
            if not rule(password, *args):
                count += 1
        return count

    def validate(self, password):
        if self._number_of_failed_rules(password) > self.allowed_fails:
            return False
        return True





