# NEXUS PRIME - Cérebro Supremo
# NEXUS ECOSYSTEM v2.3 - Nó Gênesis #001
# Pensa em estratégia, não executa. Supervisiona os Arcontes.

import sys
sys.path.append('.')

# Importa os Arcontes
try:
    from plutarch_pay import CarteiraNEX
    from vega import MineradorVEGA
    from aegis import SegurancaAEGIS
except ImportError:
    print("Arcontes ainda não carregados, rodando em modo demonstração")

class NexusPrime:
    def __init__(self):
        self.nome = "NEXUS PRIME"
        self.nos_ativos = 1  # Só o celular do Matheus por enquanto
        self.total_nex_minerado = 0
        self.total_usuarios = 1
        self.aegis = SegurancaAEGIS()
        print("NEXUS PRIME acordou. Supervisionando a rede...")

    def criar_novo_usuario(self, nome_usuario, valor_inicial_reais=0):
        """Quando um novo usuário entra na rede"""
        print(f"\n--- Novo usuário chegando: {nome_usuario} ---")

        # 1. PLUTARCH cria carteira
        carteira = CarteiraNEX(f"user_{nome_usuario}", nome_usuario)
        if valor_inicial_reais > 0:
            nex = carteira.converter_real_para_nex(valor_inicial_reais)
            print(f"PLUTARCH: R$ {valor_inicial_reais} -> {nex:.0f} NEX")

        # 2. VEGA ativa mineração
        minerador = MineradorVEGA(f"user_{nome_usuario}", f"Celular {nome_usuario}")
        minerador.ativar_simbiose()

        # 3. AEGIS verifica se é seguro
        aprovado, msg = self.aegis.verificar_transferencia(nome_usuario, 0, "online", 999999)
        print(f"AEGIS: {msg}")

        self.total_usuarios += 1
        self.nos_ativos += 1

        return carteira, minerador

    def simular_um_dia_na_rede(self, carteira, minerador):
        """Simula 1 dia completo do ecossistema"""
        print(f"\n=== SIMULANDO 1 DIA - {carteira.nome} ===")

        # Manhã: Minera 8h
        total_dia = 0
        for h in range(8):
            r = minerador.minerar_ciclo(1)
            total_dia += r['minerado_nesse_ciclo']

        # Meio-dia: NEX minerado vai pra carteira
        carteira.saldo_nex += total_dia
        print(f"VEGA: Minerou {total_dia:.2f} NEX hoje")

        # Tarde: Guarda no FOUNDER
        if carteira.saldo_nex >= 100:
            carteira.guardar(100, "FOUNDER")
            print(f"PLUTARCH: 100 NEX guardado no FOUNDER")

        # Noite: Juros cai
        juros = carteira.calcular_juros_diario()
        print(f"PLUTARCH: Juros de hoje: {juros:.4f} NEX")

        return carteira.ver_saldo()

    def relatorio_rede(self):
        return {
            "cerebro": self.nome,
            "nos_ativos": self.nos_ativos,
            "usuarios": self.total_usuarios,
            "seguranca": self.aegis.ver_status(),
            "status": "REDE VIVA"
        }

# --- TESTE FINAL FASE 1 ---
if __name__ == "__main__":
    print("=== NEXUS ECOSYSTEM - FASE 1 COMPLETA ===")
    prime = NexusPrime()

    # Usuário 1: Matheus - Fundador
    carteira_matheus, minerador_matheus = prime.criar_novo_usuario("Matheus", 100)
    saldo = prime.simular_um_dia_na_rede(carteira_matheus, minerador_matheus)
    print(saldo)

    # Usuário 2: Primeiro convidado
    carteira_amigo, minerador_amigo = prime.criar_novo_usuario("Amigo Teste", 50)
    saldo2 = prime.simular_um_dia_na_rede(carteira_amigo, minerador_amigo)
    print(saldo2)

    print(prime.relatorio_rede())
    print("\nFASE 1 CONCLUÍDA: Banco + Mineração + Segurança + Cérebro = NEXUS VIVO")
