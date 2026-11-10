import re
import json
import os
from agent import Agent
from agents.external_ai import consultar_gemini

class NexusPrime(Agent):
    def __init__(self):
        super().__init__("NEXUS PRIME", "Estrategia", "Decisor")
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
                    if "limite_roi" not in data:
                        data["limite_roi"] = 30.0
                    return data
            except Exception:
                pass
        return {"erros_aprendidos": [], "vitorias": [], "limite_roi": 30.0}

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
        if "roi" in task_lower or "investimento" in task_lower:
            numeros = re.findall(r"\d+(?:\.\d+)?", task_lower)
            if len(numeros) >= 2:
                investimento = float(numeros[0])
                retorno = float(numeros[1])
                roi = ((retorno - investimento) / investimento * 100) if investimento != 0 else 0
            elif len(numeros) == 1:
                roi = float(numeros[0])
            else:
                roi = 0
            limite = self.memoria.get("limite_roi", 30.0)
            if roi >= limite:
                self.memoria["vitorias"].append(task)
                self.salvar_memoria()
                return f"NEXUS PRIME APROVOU: ROI {roi:.1f}% acima do limite {limite}%."
            else:
                self.memoria["erros_aprendidos"].append(task)
                self.salvar_memoria()
                return f"NEXUS PRIME REJEITOU: ROI {roi:.1f}% abaixo do limite {limite}%."
        if "funil" in task_lower:
            return "NEXUS PRIME: Funil criado: Atracao > Captura > Venda > Pos-venda."
        if "buscar" in task_lower or "dados" in task_lower:
            return "NEXUS PRIME: Dados buscados e analisados."
        return f"NEXUS PRIME executou: {task}"
