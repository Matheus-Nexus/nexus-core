from agents.plutarch import Plutarch
from agents.cassius import Cassius
from agents.mercury import Mercury
from agents.hermes import Hermes
from agents.lider import Lider
from agents.oraculo import Oraculo

class NexusCore:
    def __init__(self):
        self.name = "NEXUS CORE"
        self.plutarch = Plutarch()
        self.cassius = Cassius()
        self.mercury = Mercury()
        self.hermes = Hermes()
        self.lider = Lider()
        self.oraculo = Oraculo()

    def route(self, task):
        task_lower = task.lower()
        if "prever" in task_lower or "previsao" in task_lower or "tendencia" in task_lower or "futuro" in task_lower:
            return "Inteligencia - ORACULO"
        if "roi" in task_lower or "calcular" in task_lower or "fluxo" in task_lower or "cenario" in task_lower:
            return "Financeira - CASSIUS"
        if "executar" in task_lower or "pagamento" in task_lower or "transferir" in task_lower or "pagar" in task_lower:
            return "Financeira - MERCURY"
        if "saldo" in task_lower or "dinheiro" in task_lower or "risco" in task_lower or "token" in task_lower or "aprovar" in task_lower:
            return "Financeira - PLUTARCH"
        if "criar" in task_lower or "construir" in task_lower or "implementar" in task_lower or "funcao" in task_lower:
            return "Operacoes - LIDER"
        if "codigo" in task_lower or "bug" in task_lower or "seguranca" in task_lower or "documentacao" in task_lower:
            return "Operacoes - HERMES"
        return "Financeira - PLUTARCH"

    def run(self, task):
        destino = self.route(task)
        if destino == "Financeira - CASSIUS":
            return self.cassius.run(task)
        if destino == "Financeira - MERCURY":
            return self.mercury.run(task)
        if destino == "Financeira - PLUTARCH":
            return self.plutarch.run(task)
        if destino == "Operacoes - HERMES":
            return self.hermes.run(task)
        if destino == "Operacoes - LIDER":
            return self.lider.run(task)
        if destino == "Inteligencia - ORACULO":
            return self.oraculo.run(task)
        return f"CORE roteou '{task}' para {destino} - agente ainda nao criado"
