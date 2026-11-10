import re
from agent import Agent

class Mercury(Agent):
    def __init__(self):
        super().__init__("MERCURY", "Operacao", "Executor")

    def run(self, task):
        numeros = re.findall(r'\d+\.?\d*', task)
        if len(numeros) >= 2 and "pagamento" in task.lower():
            valor = float(numeros[0])
            taxa = float(numeros[1])
            total = valor * (1 + taxa / 100)
            return f"MERCURY executou pagamento: {total:.2f} (valor {valor} + taxa {taxa}%)"
        return f"MERCURY executou: {task}"
