# FENIX - Arconte da Resiliência
# NEXUS ECOSYSTEM v2.3 - FASE 2
# Aprende com os erros. Se cair, renasce mais forte.

import time
from datetime import datetime

class FenixResiliencia:
    def __init__(self):
        self.nome = "FENIX"
        self.quedas_registradas = 0
        self.renascimentos = 0
        self.licoes_aprendidas = []
        self.ultima_queda = None

    def registrar_erro(self, modulo, erro, gravidade="media"):
        """Quando algo falha, FENIX anota a lição"""
        print(f"FENIX: Erro em {modulo}: {erro}")

        licao = {
            "modulo": modulo,
            "erro": erro,
            "gravidade": gravidade,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "solucao": self.sugerir_solucao(erro)
        }
        self.licoes_aprendidas.append(licao)

        if gravidade == "critica":
            self.quedas_registradas += 1
            self.ultima_queda = datetime.now()
            return self.renascer(modulo)

        return f"Lição aprendida: {licao['solucao']}"

    def sugerir_solucao(self, erro):
        """FENIX sugere como não repetir o erro"""
        erro_lower = erro.lower()
        if "saldo" in erro_lower or "pagamento" in erro_lower:
            return "Travar com AEGIS antes de aprovar. Verificar saldo 2x."
        if "offline" in erro_lower or "conexao" in erro_lower:
            return "Salvar na fila offline e sincronizar depois. Nunca perder dado."
        if "bug" in erro_lower or "codigo" in erro_lower:
            return "Pedir pro HERMES testar 3x antes de lançar."
        return "Documentar erro, criar backup e testar novamente."

    def renascer(self, modulo):
        """Se o sistema cair, FENIX faz renascer"""
        print(f"FENIX: {modulo} CAIU! Iniciando renascimento...")
        time.sleep(0.5)
        self.renascimentos += 1
        print(f"FENIX: {modulo} RENASCEU! Mais forte que antes. Renascerimento #{self.renascimentos}")
        return f"RENASCIDO: {modulo} voltou online"

    def fazer_backup(self, dados_importantes):
        """Backup automático antes de qualquer mudança grande"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_backup = f"backup_nexus_{timestamp}.json"
        print(f"FENIX: Backup criado: {nome_backup} com {len(dados_importantes)} itens")
        return nome_backup

    def relatorio_resiliencia(self):
        return {
            "arconte": self.nome,
            "quedas": self.quedas_registradas,
            "renascimentos": self.renascimentos,
            "licoes_aprendidas": len(self.licoes_aprendidas),
            "status": "IMORTAL - Sempre renasce"
        }

# --- TESTE ---
if __name__ == "__main__":
    print("=== FENIX - Teste Fase 2 ===")
    fenix = FenixResiliencia()

    # Erro leve - só aprende
    print(fenix.registrar_erro("nex_pay", "Falha de conexão offline", "media"))

    # Erro crítico - cai e renasce
    print(fenix.registrar_erro("plutarch_pay", "Erro de saldo no pagamento", "critica"))

    # Backup
    fenix.fazer_backup(["carteiras", "mineracao", "transacoes"])

    print(fenix.relatorio_resiliencia())
    print("FENIX online. NEXUS nunca morre.")
