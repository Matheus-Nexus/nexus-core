class NexusCore:
    def __init__(self):
        self.name = "NEXUS CORE"

    def route(self, task):
        task = task.lower()
        if "saldo" in task or "dinheiro" in task or "roi" in task or "risco" in task or "token" in task:
            return "Financeira - PLUTARCH"
        if "codigo" in task or "bug" in task or "seguranca" in task or "documentacao" in task:
            return "Operacoes - HERMES"
        return "Financeira - PLUTARCH"

    def run(self, task):
        destino = self.route(task)
        return f"CORE roteou '{task}' para {destino}"
