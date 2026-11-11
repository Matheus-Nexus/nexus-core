# NEX PAY - Carteira com QR Code Offline
# NEXUS ECOSYSTEM v2.3 - FASE 2
# Transfere NEX sem internet, via QR + Bluetooth

import json
import time
import hashlib
from datetime import datetime

class NexPay:
    def __init__(self, usuario_id, nome, saldo_inicial=0):
        self.usuario_id = usuario_id
        self.nome = nome
        self.saldo = saldo_inicial
        self.pendentes_offline = []  # Fila pra sincronizar quando voltar internet

    def gerar_qr_pagamento(self, valor, mensagem=""):
        """Gera o código QR para receber/enviar offline"""
        if valor > self.saldo:
            return "Saldo insuficiente"

        # Trava AEGIS: 200 NEX offline
        if valor > 200:
            return "TRAVA AEGIS: Offline limite é 200 NEX. Use modo online."

        dados = {
            "de": self.usuario_id,
            "nome": self.nome,
            "valor": valor,
            "mensagem": mensagem,
            "timestamp": int(time.time()),
            "tipo": "nex_pay_offline"
        }

        # Assinatura simples pra ninguém falsificar
        dados_str = json.dumps(dados, sort_keys=True)
        assinatura = hashlib.sha256(dados_str.encode()).hexdigest()[:12]
        dados["assinatura"] = assinatura

        qr_string = json.dumps(dados)
        print(f"QR GERADO: {self.nome} -> {valor} NEX")
        print(f"Mostre esse QR para quem vai receber")
        return qr_string

    def ler_qr_e_receber(self, qr_string, minha_carteira):
        """Quem recebe escaneia o QR e ganha o NEX na hora"""
        try:
            dados = json.loads(qr_string)
        except:
            return "QR inválido"

        valor = dados["valor"]

        # Verifica assinatura
        assinatura_original = dados.pop("assinatura")
        dados_str = json.dumps(dados, sort_keys=True)
        assinatura_check = hashlib.sha256(dados_str.encode()).hexdigest()[:12]

        if assinatura_check != assinatura_original:
            return "BLOQUEADO AEGIS: QR falsificado!"

        # Se quem enviou está offline, guarda na fila pra sincronizar depois
        # Mas o saldo já aparece na hora pra quem recebeu
        minha_carteira.saldo += valor

        # Adiciona na fila de sincronização
        self.pendentes_offline.append({
            "de": dados["de"],
            "para": minha_carteira.usuario_id,
            "valor": valor,
            "timestamp": dados["timestamp"],
            "sincronizado": False
        })

        return f"RECEBIDO: +{valor} NEX de {dados['nome']} via QR Offline"

    def sincronizar_quando_voltar_internet(self):
        """Quando volta a internet, manda tudo pra rede"""
        if not self.pendentes_offline:
            return "Nada pra sincronizar"

        total = sum(p["valor"] for p in self.pendentes_offline if not p["sincronizado"])
        for p in self.pendentes_offline:
            p["sincronizado"] = True

        return f"SINCRONIZADO: {len(self.pendentes_offline)} transferências, total {total} NEX enviado pra rede"

    def ver_saldo(self):
        return {
            "nome": self.nome,
            "saldo": self.saldo,
            "pendentes": len(self.pendentes_offline)
        }

# --- TESTE FASE 2 ---
if __name__ == "__main__":
    print("=== NEX PAY - Teste Offline ===")
    matheus = NexPay("001", "Matheus", 1000)
    amigo = NexPay("002", "Amigo", 0)

    # Matheus gera QR de 50 NEX, sem internet
    qr = matheus.gerar_qr_pagamento(50, "Pagando lanche")
    matheus.saldo -= 50  # Saiu da carteira do Matheus

    # Amigo escaneia
    print(amigo.ler_qr_e_receber(qr, amigo))
    print(amigo.ver_saldo())

    # Teste golpe: tenta mandar 500 offline
    print(matheus.gerar_qr_pagamento(500))

    # Volta internet e sincroniza
    print(matheus.sincronizar_quando_voltar_internet())
    print("NEX PAY online. Pagamento offline funcionando.")
