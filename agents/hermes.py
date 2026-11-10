from agent import Agent

class Hermes(Agent):
    def __init__(self):
        super().__init__("HERMES", "Operacoes", "Diretor de Operacoes")

    def run(self, task):
        return f"HERMES coordenou operacao: {task}"
