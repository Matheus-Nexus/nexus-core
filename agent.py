class Agent:
    def __init__(self, name, division, role):
        self.name = name
        self.division = division
        self.role = role

    def run(self, task):
        return f"{self.name} executou: {task}"
