import re
from agent import Agent

class Plutarch(Agent):
    def __init__(self):
        super().__init__("PLUTARCH", "Financeira", "Aprovador")

    def run(self, task):
        numeros = re.findall(r'\d+\.?\d*', task)
        if len(numeros) >= 2 and "saldo" in task.lower():
            inicial = float(numeros[0])
            gasto = float(numeros[1])
            saldo = inicial - gasto
            return f"PLUTARCH analisou saldo: {saldo:.2f} (inicial {inicial} - gasto {gasto})"
        return f"PLUTARCH aprovou e coordenou: {task}"
