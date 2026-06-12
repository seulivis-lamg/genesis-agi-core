class DecisionEngine:
    def __init__(self):
        pass

    def evaluate(self, options):
        if not options:
            return None

        return options[0]

    def assess_risk(self, option):
        return "low"
