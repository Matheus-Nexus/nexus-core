# PLUTARCH - Arconte do Banco
# NEXUS ECOSYSTEM v2.3 - Nó Gênesis #001
# Cuida da carteira, conversão e NEX Guardado

import time
import json
from datetime import datetime

# --- CONFIGURAÇÃO OFICIAL DO DOCUMENTO ---
TOTAL_NEX = 1_000_000_000
COFRES = {
    "mineracao": 0.40,
    "reserva": 0.20,
    "expansao": 0.15,
    "autodesenvolvimento": 0.15,
    "equipe": 0.10
}

# Preço inicial: 1 NEX = R$ 0,10
PRECO_NEX_BRL = 0.10

PLANOS = {
    "START": {"minimo": 100, "juros_mensal": 0.005, "simbiose": False},
    "PLUS": {"minimo": 1000, "juros_mensal": 0.012, "simbiose": True},
    "PRIME": {"minimo": 10000, "juros_mensal": 0.020, "simbiose": True},
    "FOUNDER": {"minimo": 100, "juros_mensal": 0.025, "simbiose": True, "bonus": 50, "limite_bonus": 5000}
}

class CarteiraNEX:
    def __init__(self, usuario_id, nome):
        self.usuario_id = usuario_id
        self.nome = nome
        self.saldo_nex = 0.0
        self.guardado = 0.0
        self.plano = None
        self.e_founder = False
        self.simbiose_ativa = False
        self.historico = []

    def converter_real_para_nex(self, valor_reais):
        """Converte Real em NEX - NEX Pay Exchange"""
        nex_recebido = valor_reais / PRECO_NEX_BRL
        self.saldo_nex += nex_recebido
        self._registrar(f"Conversão: R$ {valor_reais} -> {nex_recebido:.2f} NEX")
        return nex_recebido

    def converter_cripto_para_nex(self, valor_cripto, preco_cripto_brl):
        """Converte qualquer cripto em NEX via valor em Reais"""
        valor_reais = valor_cripto * preco_cripto_brl
        return self.converter_real_para_nex(valor_reais)

    def transferir(self, destino, valor, modo="online"):
        """Transferência NEX para NEX - online / offline / bluetooth"""
        if valor > self.saldo_nex:
            return "Saldo insuficiente"

        # Trava de segurança do documento
        if modo in ["offline", "bluetooth"] and valor > 200:
            return "TRAVA AEGIS: Offline/Bluetooth limite é 200 NEX"

        self.saldo_nex -= valor
        destino.saldo_nex += valor

        self._registrar(f"Enviou {valor} NEX para {destino.nome} via {modo}")
        destino._registrar(f"Recebeu {valor} NEX de {self.nome} via {modo}")
        return f"OK: {valor} NEX enviado via {modo}"

    def ativar_simbiose(self):
        """Celular vira mini-servidor"""
        self.simbiose_ativa = True
        self._registrar("Simbiose ativada - Celular virou mini-servidor")
        return "Mini-servidor ativado! Mineração potencializada."

    def guardar(self, valor, plano_nome):
        """NEX Guardado - Juros com liquidez diária"""
        plano = PLANOS.get(plano_nome)
        if not plano:
            return "Plano não existe"
        if valor < plano["minimo"]:
            return f"Mínimo do {plano_nome} é {plano['minimo']} NEX"
        if valor > self.saldo_nex:
            return "Saldo insuficiente"

        self.saldo_nex -= valor
        self.guardado += valor
        self.plano = plano_nome

        # Bônus FOUNDER
        if plano_nome == "FOUNDER":
            self.e_founder = True
            self.guardado += plano["bonus"]
            self._registrar(f"Bônus FOUNDER: +{plano['bonus']} NEX")

        self._registrar(f"Guardado {valor} NEX no plano {plano_nome}")
        return f"OK: {valor} NEX guardado no {plano_nome}"

    def calcular_juros_diario(self):
        """Calcula juros de 1 dia"""
        if not self.plano or self.guardado == 0:
            return 0
        taxa = PLANOS[self.plano]["juros_mensal"]
        juros_dia = self.guardado * (taxa / 30)
        self.guardado += juros_dia
        return juros_dia

    def _registrar(self, msg):
        self.historico.append(f"{datetime.now().strftime('%d/%m %H:%M')} - {msg}")

    def ver_saldo(self):
        return {
            "usuario": self.nome,
            "saldo_livre": round(self.saldo_nex, 2),
            "guardado": round(self.guardado, 2),
            "plano": self.plano,
            "simbiose": self.simbiose_ativa,
            "total": round(self.saldo_nex + self.guardado, 2)
        }

# --- TESTE DO NÓ GÊNESIS ---
if __name__ == "__main__":
    print("=== NEXUS - Teste Nó Gênesis #001 ===")
    matheus = CarteiraNEX("001", "Matheus - Fundador")
    matheus.converter_real_para_nex(100)  # R$100 -> 1000 NEX
    matheus.ativar_simbiose()
    matheus.guardar(1000, "FOUNDER")
    print(matheus.ver_saldo())
    print(f"Juros de 1 dia: {matheus.calcular_juros_diario():.4f} NEX")
    print("PLUTARCH online. Banco NEX funcionando.")
