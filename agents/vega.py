# VEGA - Arconte da Mineração
# NEXUS ECOSYSTEM v2.3 - Nó Gênesis #001
# Faz o celular minerar como mini-servidor

import time
import random
from datetime import datetime

class MineradorVEGA:
    def __init__(self, usuario_id, nome):
        self.usuario_id = usuario_id
        self.nome = nome
        self.simbiose_ativa = False
        self.total_minerado = 0.0
        self.validacoes = 0
        self.aprendizados = 0
        self.memoria_guardada = 0
        self.historico = []

    def ativar_simbiose(self):
        self.simbiose_ativa = True
        print(f"[{self.nome}] Simbiose ativada - Celular virou mini-servidor #001")
        return True

    def minerar_ciclo(self, horas=1):
        """1 ciclo = 1 hora de celular como mini-servidor"""
        if not self.simbiose_ativa:
            return "Ative a simbiose primeiro!"

        # 1. Validar transferências - 40% da recompensa
        validacoes_hora = random.randint(80, 150)
        recompensa_validar = validacoes_hora * 0.008  # 0,008 NEX por validação

        # 2. Aprender offline - 35% da recompensa
        aprendizados_hora = random.randint(3, 8)
        recompensa_aprender = aprendizados_hora * 0.15

        # 3. Guardar memória - 25% da recompensa
        memoria_hora = random.randint(5, 15)
        recompensa_memoria = memoria_hora * 0.05

        total_ciclo = recompensa_validar + recompensa_aprender + recompensa_memoria

        self.validacoes += validacoes_hora
        self.aprendizados += aprendizados_hora
        self.memoria_guardada += memoria_hora
        self.total_minerado += total_ciclo

        self.historico.append(f"{datetime.now().strftime('%H:%M')} - Minerou {total_ciclo:.2f} NEX em {horas}h")

        return {
            "minerado_nesse_ciclo": round(total_ciclo, 2),
            "validacoes": validacoes_hora,
            "aprendizados": aprendizados_hora,
            "memoria": memoria_hora,
            "total_minerado": round(self.total_minerado, 2)
        }

    def ver_status(self):
        return {
            "minerador": self.nome,
            "simbiose": "ATIVA" if self.simbiose_ativa else "DESATIVADA",
            "total_minerado": round(self.total_minerado, 2),
            "validacoes": self.validacoes,
            "aprendizados": self.aprendizados,
            "memoria_guardada": self.memoria_guardada
        }

# --- TESTE NÓ GÊNESIS ---
if __name__ == "__main__":
    print("=== VEGA - Teste Nó Gênesis #001 ===")
    celular_matheus = MineradorVEGA("001", "Celular Matheus - Nó #001")
    celular_matheus.ativar_simbiose()

    # Simula 8 horas de celular rodando
    for hora in range(1, 9):
        resultado = celular_matheus.minerar_ciclo(1)
        print(f"Hora {hora}: +{resultado['minerado_nesse_ciclo']} NEX")

    print(celular_matheus.ver_status())
    print("VEGA online. Mineração potencializada pela simbiose.")
