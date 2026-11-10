from agent import Agent

class Mercury(Agent):
    def __init__(self):
        super().__init__("MERCURY", "Financeira", "Executor")

    def run(self, task):
        return f"MERCURY executou: {task}"
