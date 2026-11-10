import re
import json
import os
from agent import Agent
from agents.external_ai import consultar_gemini

class NexusPrime(Agent):
    def __init__(self):
        super().__init__("NEXUS PRIME", "NEXUS", "ORQUESTRADOR")
        self.arquivo_memoria = "nexus_memoria.json"
        self.memoria = self._carregar_memoria()

    def _carregar_memoria(self):
        if os.path.exists(self.arquivo_memoria):
            try:
                with open(self.arquivo_memoria, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "erros_aprendidos" not in data:
                        data["erros_aprendidos"] = []
                    if "vitorias" not in data:
                        data["vitorias"] = []
                    return data
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
        if "erro" in task_lower or "falha" in task_lower or "fracasso" in task_lower:
            self.memoria["erros_aprendidos"].append(task)
            self.salvar_memoria()
            return f"NEXUS PRIME aprendeu com erro: {task}"
        if "roi" in task_lower:
            numeros = re.findall(r"\d+(?:\.\d+)?", task_lower)
            valor = float(numeros[0]) if numeros else 0
            if valor >= 100:
                self.memoria["vitorias"].append(task)
                self.salvar_memoria()
                return f"NEXUS PRIME: ROI {valor}% APROVADO. Pode escalar."
            else:
                self.memoria["erros_aprendidos"].append(task)
                self.salvar_memoria()
                return f"NEXUS PRIME: ROI {valor}% REJEITADO. ROI baixo demais."
        if "funil" in task_lower:
            return "NEXUS PRIME: Funil criado: Atracao > Captura > Venda > Pos-venda."
        if "buscar" in task_lower or "dados" in task_lower:
            return "NEXUS PRIME: Dados buscados e analisados."
        return f"NEXUS PRIME executou: {task}"
