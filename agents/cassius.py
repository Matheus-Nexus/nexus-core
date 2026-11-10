from agent import Agent

class Cassius(Agent):
    def __init__(self):
        super().__init__("CASSIUS", "Financeira", "Analista")

    def run(self, task):
        return f"CASSIUS calculou: {task}"
