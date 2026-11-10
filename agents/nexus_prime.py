import os
import json
import re
from datetime import datetime
from agents.external_ai import consultar_gemini

ARQUIVO_MEMORIA = "memoria.json"

class NexusPrime:
    def __init__(self):
        self.name = "NEXUS PRIME"
        self.division = "Estrategia"
        self.memoria = {"limite_roi": 30.0}
        # Carrega historico salvo em arquivo, se existir
        try:
            if os.path.exists(ARQUIVO_MEMORIA):
                with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
                    historico = json.load(f)
                    if isinstance(historico, list) and historico:
                        self.memoria["historico"] = historico
        except:
            pass

    def _salvar_aprendizado(self, pergunta, resposta):
        historico = self.memoria.get("historico", [])
        if not isinstance(historico, list):
            historico = []
        historico.append({
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "pergunta": pergunta,
            "aprendizado": resposta
        })
        historico = historico[-20:]
        self.memoria["historico"] = historico
        try:
            with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
                json.dump(historico, f, ensure_ascii=False, indent=2)
        except:
            pass
        return len(historico)

    def run(self, task):
        task_lower = task.lower()

        # 1. CONSULTAR IA EXTERNA - com memoria
        if "consultar" in task_lower or "ia externa" in task_lower or "gemini" in task_lower:
            pergunta = task.replace("consultar IA externa:", "").replace("consultar ia externa:", "").strip()
            if not pergunta:
                pergunta = task
            resposta = consultar_gemini(pergunta)
            total = self._salvar_aprendizado(pergunta, resposta)
            return f"NEXUS PRIME consultou IA externa e aprendeu: {resposta} [Memoria salva! Total de aprendizados: {total}]"

        # 2. DECIDIR ESTRATEGIA - usa limite_roi da memoria
        if "decidir" in task_lower or "estrategia" in task_lower:
            limite = self.memoria.get("limite_roi", 30.0)
            numeros = re.findall(r"\d+", task)
            if len(numeros) >= 2:
                investimento = float(numeros[0])
                retorno = float(numeros[1])
                if investimento == 0:
                    return "NEXUS PRIME analisou estrategia."
                roi = (retorno - investimento) / investimento * 100
                if roi >= limite:
                    return f"NEXUS PRIME APROVOU: ROI {roi:.1f}% acima do limite {limite:.1f}%."
                else:
                    return f"NEXUS PRIME REJEITOU: ROI {roi:.1f}% abaixo do limite {limite:.1f}%."
            return "NEXUS PRIME analisou estrategia."

        # 3. APRENDER COM ERRO
        if "erro" in task_lower or "falha" in task_lower or "bug" in task_lower:
            total = self._salvar_aprendizado(task, f"Erro registrado: {task}")
            return f"NEXUS PRIME aprendeu com erro: {task} [Memoria salva! Total: {total}]"

        return "NEXUS PRIME analisou a tarefa."
