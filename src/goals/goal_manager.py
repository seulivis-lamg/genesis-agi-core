class GoalManager:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def get_goals(self):
        return self.goals

    def remove_goal(self, goal):
        if goal in self.goals:
            self.goals.remove(goal)
