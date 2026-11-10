from agent import Agent

class Oraculo(Agent):
    def __init__(self):
        super().__init__("ORACULO", "Inteligencia", "Analista de Dados")

    def run(self, task):
        return f"ORACULO previu: {task}"
