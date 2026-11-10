import re
from agent import Agent

class Cassius(Agent):
    def __init__(self):
        super().__init__("CASSIUS", "Financeira", "Analista Financeiro")

    def run(self, task):
        numeros = re.findall(r'\d+\.?\d*', task)
        if len(numeros) >= 2 and "roi" in task.lower():
            investimento = float(numeros[0])
            retorno = float(numeros[1])
            if investimento == 0:
                return "CASSIUS: investimento nao pode ser zero"
            roi = ((retorno - investimento) / investimento) * 100
            return f"CASSIUS calculou ROI: {roi:.1f}% (investimento {investimento} -> retorno {retorno})"
        return f"CASSIUS calculou: {task}"
