from agent import Agent

class Lider(Agent):
    def __init__(self):
        # MANTÉM ESSA LINHA IGUAL A QUE JÁ ESTÁ NO SEU ARQUIVO
        super().__init__("LIDER", "Engenharia", "Construtor")

    def run(self, task):
        if "login" in task.lower() and "criar" in task.lower():
            return 'LIDER criou funcao login:\ndef login(usuario, senha):\n    return usuario == "admin" and senha == "1234"'
        return f"LIDER construiu: {task}"
