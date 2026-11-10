from agents.plutarch import Plutarch
from agents.cassius import Cassius

class NexusCore:
    def __init__(self):
        self.name = "NEXUS CORE"
        self.plutarch = Plutarch()
        self.cassius = Cassius()

    def route(self, task):
        task_lower = task.lower()
        if "roi" in task_lower or "calcular" in task_lower or "fluxo" in task_lower or "cenario" in task_lower:
            return "Financeira - CASSIUS"
        if "saldo" in task_lower or "dinheiro" in task_lower or "risco" in task_lower or "token" in task_lower or "aprovar" in task_lower:
            return "Financeira - PLUTARCH"
        if "codigo" in task_lower or "bug" in task_lower or "seguranca" in task_lower or "documentacao" in task_lower:
            return "Operacoes - HERMES"
        return "Financeira - PLUTARCH"

    def run(self, task):
        destino = self.route(task)
        if destino == "Financeira - CASSIUS":
            return self.cassius.run(task)
        if destino == "Financeira - PLUTARCH":
            return self.plutarch.run(task)
        return f"CORE roteou '{task}' para {destino} - agente ainda nao criado"
