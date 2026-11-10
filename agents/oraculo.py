import re
from agent import Agent

class Oraculo(Agent):
    def __init__(self):
        super().__init__("ORACULO", "Inteligencia", "Estrategista")

    def run(self, task):
        numeros = re.findall(r'\d+\.?\d*', task)
        if len(numeros) >= 2 and "prever" in task.lower():
            atual = float(numeros[0])
            crescimento = float(numeros[1])
            futuro = atual * (1 + crescimento / 100)
            return f"ORACULO previu preco futuro: {futuro:.2f} (atual {atual} + {crescimento}%)"
        return f"ORACULO previu: {task}"
