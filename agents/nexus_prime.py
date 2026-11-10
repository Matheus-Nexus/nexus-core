from agent import Agent

class NexusPrime(Agent):
    def __init__(self):
        super().__init__("NEXUS PRIME", "Direcao", "CEO")

    def run(self, task):
        return f"NEXUS PRIME decidiu: {task}"
