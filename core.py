from agents.cassius import Cassius
from agents.mercury import Mercury
from agents.plutarch import Plutarch
from agents.hermes import Hermes
from agents.oraculo import Oraculo
from agents.lider import Lider
from agents.nexus_prime import NexusPrime

class NexusCore:
    def __init__(self):
        self.agents = {
            "Financeira - CASSIUS": Cassius(),
            "Financeira - MERCURY": Mercury(),
            "Financeira - PLUTARCH": Plutarch(),
            "Operacoes - HERMES": Hermes(),
            "Operacoes - ORACULO": Oraculo(),
            "Operacoes - LIDER": Lider(),
            "Estrategia - NEXUS PRIME": NexusPrime(),
        }

    def route(self, task):
        task_lower = task.lower()
        if "consultar" in task_lower or "ia externa" in task_lower or "gemini" in task_lower:
            return "Estrategia - NEXUS PRIME"
        if "decidir" in task_lower or "estrategia" in task_lower or "erro" in task_lower or "falha" in task_lower or "bug" in task_lower:
            return "Estrategia - NEXUS PRIME"
        if "roi" in task_lower or "investimento" in task_lower:
            return "Financeira - CASSIUS"
        if "pagamento" in task_lower or "pagar" in task_lower:
            return "Financeira - MERCURY"
        if "saldo" in task_lower:
            return "Financeira - PLUTARCH"
        if "codigo" in task_lower or "contar" in task_lower or "palavras" in task_lower:
            return "Operacoes - HERMES"
        if "preco" in task_lower or "prever" in task_lower:
            return "Operacoes - ORACULO"
        if "criar" in task_lower or "funcao" in task_lower or "login" in task_lower:
            return "Operacoes - LIDER"
        return "Financeira - PLUTARCH"

    def run(self, task):
        agent_key = self.route(task)
        agent = self.agents[agent_key]
        return agent.run(task)
