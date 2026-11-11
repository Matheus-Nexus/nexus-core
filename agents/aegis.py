# AEGIS - Arconte da Segurança
# NEXUS ECOSYSTEM v2.3 - Nó Gênesis #001
# Paranoico, desconfiado. Trava tudo que for perigoso.

from datetime import datetime

class SegurancaAEGIS:
    def __init__(self):
        self.tentativas_bloqueadas = 0
        self.lista_negra = []
        self.limite_offline = 200  # Regra do documento
        self.limite_por_pessoa_founder = 5000

    def verificar_transferencia(self, remetente, valor, modo, saldo_remetente):
        """Verifica se a transferência é segura antes de aprovar"""
        
        # 1. Saldo suficiente?
        if valor > saldo_remetente:
            self.tentativas_bloqueadas += 1
            return False, "BLOQUEADO: Saldo insuficiente"

        # 2. Limite offline / bluetooth - 200 NEX
        if modo in ["offline", "bluetooth"] and valor > self.limite_offline:
            self.tentativas_bloqueadas += 1
            return False, f"BLOQUEADO: Offline limite é {self.limite_offline} NEX"

        # 3. Usuário está na lista negra?
        if remetente in self.lista_negra:
            return False, "BLOQUEADO: Usuário na lista negra"

        # 4. Valor absurdo? Ex: 1 milhão de uma vez
        if valor > 100000:
            return False, "BLOQUEADO: Precisa de aprovação do PLUTARCH para valor alto"

        return True, "APROVADO por AEGIS"

    def verificar_promocao_founder(self, total_gasto_expansao, teto_expansao=30000000):
        """Trava a promoção FOUNDER se acabar o cofre de Expansão"""
        if total_gasto_expansao >= teto_expansao:
            return False, "PROMOÇÃO ENCERRADA: Cofre de Expansão esgotado"
        restantes = teto_expansao - total_gasto_expansao
        return True, f"Promoção ativa. Restam {restantes} NEX no cofre"

    def verificar_guardado(self, valor, plano, total_guardado_founder):
        """Trava juro de 2,5% só até 5.000 NEX por pessoa"""
        if plano == "FOUNDER" and total_guardado_founder + valor > self.limite_por_pessoa_founder:
            return False, "BLOQUEADO: Limite FOUNDER é 5.000 NEX com 2,5%"
        return True, "Guardado aprovado"

    def banir_usuario(self, usuario_id, motivo):
        self.lista_negra.append(usuario_id)
        return f"Usuário {usuario_id} banido. Motivo: {motivo}"

    def ver_status(self):
        return {
            "tentativas_bloqueadas": self.tentativas_bloqueadas,
            "usuarios_banidos": len(self.lista_negra),
            "status": "VIGILANTE 24H"
        }

# --- TESTE ---
if __name__ == "__main__":
    print("=== AEGIS - Teste Nó Gênesis #001 ===")
    aegis = SegurancaAEGIS()

    # Teste 1: Transferência normal - deve aprovar
    print(aegis.verificar_transferencia("001", 100, "online", 1000))

    # Teste 2: Golpe offline - deve bloquear
    print(aegis.verificar_transferencia("001", 500, "offline", 1000))

    # Teste 3: Tentando pegar juro FOUNDER demais
    print(aegis.verificar_guardado(6000, "FOUNDER", 0))

    print(aegis.ver_status())
    print("AEGIS online. Rede protegida.")
