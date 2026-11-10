from agent import Agent

class Lider(Agent):
    def __init__(self):
        super().__init__("LIDER", "Operacoes", "Engenheiro-Chefe")

    def run(self, task):
        return f"LIDER construiu: {task}"
