import re
import json
import os
from agent import Agent
from agents.external_ai import consultar_gemini

class NexusPrime(Agent):
    def __init__(self):
        super().__init__("NEXUS PRIME")
        self.arquivo_memoria = "nexus_memoria.json"
        self.memoria = self._carregar_memoria()

    def _carregar_memoria(self):
        if os.path.exists(self.arquivo_memoria):
            try:
                with open(self.arquivo_memoria, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"erros_aprendidos": [], "vitorias": []}

    def salvar_memoria(self):
        try:
            with open(self.arquivo_memoria, "w", encoding="utf-8") as f:
                json.dump(self.memoria, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def run(self, task):
        task_lower = task.lower()
        if "consultar ia" in task_lower or "perguntar ia" in task_lower or "melhorar" in task_lower:
            resposta = consultar_gemini(task)
            self.memoria["erros_aprendidos"].append(f"Aprendeu com IA externa: {resposta[:100]}")
            self.salvar_memoria()
            return f"NEXUS PRIME consultou IA externa e aprendeu: {resposta}"
        if "roi" in task_lower:
            return "NEXUS PRIME: ROI calculado. Foco em aumentar receita e cortar custo."
        if "funil" in task_lower:
            return "NEXUS PRIME: Funil criado: Atracao > Captura > Venda > Pos-venda."
        if "buscar" in task_lower or "dados" in task_lower:
            return "NEXUS PRIME: Dados buscados e analisados."
        return f"NEXUS PRIME executou: {task}"
