from agent import Agent

class Hermes(Agent):
    def __init__(self):
        super().__init__("HERMES", "Comunicacao", "Mensageiro")

    def run(self, task):
        if "contar palavras" in task.lower():
            texto = task.lower().replace("contar palavras", "").strip()
            palavras = texto.split() if texto else []
            return f"HERMES contou {len(palavras)} palavras: {texto}"
        return f"HERMES coordenou operacao: {task}"
