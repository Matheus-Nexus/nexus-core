from agent import Agent

class Plutarch(Agent):
    def __init__(self):
        super().__init__("PLUTARCH", "Financeira", "Diretor Financeiro")

    def run(self, task):
        return f"PLUTARCH aprovou e coordenou: {task}"
