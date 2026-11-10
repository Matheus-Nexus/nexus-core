import os
import json
from datetime import datetime
from agents.external_ai import consultar_gemini

ARQUIVO_MEMORIA = "memoria.json"

class NexusPrime:
    def _carregar_memoria(self):
        if not os.path.exists(ARQUIVO_MEMORIA):
            return []
        try:
            with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def _salvar_aprendizado(self, pergunta, resposta):
        memoria = self._carregar_memoria()
        memoria.append({
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "pergunta": pergunta,
            "aprendizado": resposta
        })
        # Guarda só os últimos 20 aprendizados pra não ficar gigante
        memoria = memoria[-20:]
        with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
            json.dump(memoria, f, ensure_ascii=False, indent=2)
        return len(memoria)

    def run(self, task):
        task_lower = task.lower()

        # 1. CONSULTAR IA EXTERNA - com memória
        if "consultar" in task_lower or "ia externa" in task_lower or "gemini" in task_lower:
            pergunta = task.replace("consultar IA externa:", "").replace("consultar ia externa:", "").strip()
            if not pergunta:
                pergunta = task
            resposta = consultar_gemini(pergunta)
            total = self._salvar_aprendizado(pergunta, resposta)
            return f"NEXUS PRIME consultou IA externa e aprendeu: {resposta} [Memoria salva! Total de aprendizados: {total}]"

        # 2. DECIDIR ESTRATEGIA
        if "decidir" in task_lower or "estrategia" in task_lower:
            # Usa a memória pra decidir melhor
            memoria = self._carregar_memoria()
            dica = ""
            if memoria:
                dica = f" Usando {len(memoria)} aprendizados anteriores."
            # Extrai os numeros da tarefa
            import re
            numeros = re.findall(r"\d+", task)
            if len(numeros) >= 2:
                investimento = float(numeros[0])
                retorno = float(numeros[1])
                roi = (retorno - investimento) / investimento * 100
                if roi >= 30:
                    return f"NEXUS PRIME APROVOU: ROI {roi:.1f}% acima do limite 30.0%.{dica}"
                else:
                    return f"NEXUS PRIME REJEITOU: ROI {roi:.1f}% abaixo do limite 30.0%.{dica}"
            return f"NEXUS PRIME analisou estrategia.{dica}"

        # 3. APRENDER COM ERRO
        if "erro" in task_lower or "falha" in task_lower or "bug" in task_lower:
            total = self._salvar_aprendizado(task, f"Erro registrado: {task}")
            return f"NEXUS PRIME aprendeu com erro: {task} [Memoria salva! Total: {total}]"

        return "NEXUS PRIME analisou a tarefa."
