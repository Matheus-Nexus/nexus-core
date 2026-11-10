import re
import json
import os
from agent import Agent
from agents.external_ai import consultar_gemini

class NexusPrime(Agent):
    def __init__(self):
        super().__init__("NEXUS PRIME", "Estrategia", "Decisor")
        self.memoria_arquivo = "memoria_nexus.json"
        self.memoria = self.carregar_memoria()

    def carregar_memoria(self):
        if os.path.exists(self.memoria_arquivo):
            try:
                with open(self.memoria_arquivo, "r") as f:
                    return json.load(f)
            except:
                pass
        return {"decisoes": 0, "aprovados": 0, "rejeitados": 0, "limite_roi": 30.0, "erros_aprendidos": []}

    def salvar_memoria(self):
        try:
            with open(self.memoria_arquivo, "w") as f:
                json.dump(self.memoria, f, indent=2)
        except:
            pass

    def run(self, task):
        task_lower = task.lower()

        # ELE APRENDE COM ROI
        if "roi" in task_lower or "estrategia" in task_lower or "decidir" in task_lower:
            numeros = re.findall(r'\d+\.?\d*', task)
            limite = self.memoria.get("limite_roi", 30.0)

            if len(numeros) >= 2:
                inv = float(numeros[0])
                ret = float(numeros[1])
                roi = (ret - inv) / inv * 100 if inv != 0 else 0
                self.memoria["decisoes"] += 1

                if roi >= limite:
                    self.memoria["aprovados"] += 1
                    self.salvar_memoria()
                    return f"NEXUS PRIME APROVOU: ROI {roi:.1f}% >= limite {limite:.1f}% | Memoria: {self.memoria['aprovados']} aprovados, {self.memoria['rejeitados']} rejeitados"
                else:
                    self.memoria["rejeitados"] += 1
                    # AQUI ELE APRENDE: se rejeitou muito, ele fica mais rigoroso
                    if self.memoria["rejeitados"] > 3:
                        self.memoria["limite_roi"] = limite + 5
                        self.memoria["erros_aprendidos"].append(f"Aprendeu: aumentou limite para {limite+5} apos muitos rejeitados")
                    self.salvar_memoria()
                    return f"NEXUS PRIME REJEITOU: ROI {roi:.1f}% < limite {limite:.1f}% | Aprendendo com erro..."

            self.memoria["decisoes"] += 1
            self.salvar_memoria()
            return f"NEXUS PRIME decidiu: {task} | Memoria: {self.memoria['decisoes']} decisoes, limite atual ROI {limite}%"

        # ELE APRENDE COM ERRO / BUG
        if "erro" in task_lower or "bug" in task_lower or "falha" in task_lower:
            self.memoria["erros_aprendidos"].append(task)
            self.salvar_memoria()
            return f"NEXUS PRIME aprendeu com erro: {task} | Total erros aprendidos: {len(self.memoria['erros_aprendidos'])} | Nao vou repetir."

        return f"NEXUS PRIME decidiu: {task}"

    def evoluir(self):
        """Mostra o quanto ele evoluiu"""
        return f"EVOLUCAO NEXUS PRIME: {self.memoria['decisoes']} decisoes, {self.memoria['aprovados']} aprovados, limite ROI atual: {self.memoria['limite_roi']}%, erros aprendidos: {len(self.memoria['erros_aprendidos'])}"
