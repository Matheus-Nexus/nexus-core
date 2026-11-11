# MARKETPLACE NEXUS - FASE 3
# Onde o NEX vira pão, roupa, serviço. Economia real.

class MarketplaceNexus:
    def __init__(self):
        self.produtos = []
        self.vendas = 0
        self.volume_nex = 0

    def anunciar(self, vendedor, produto, preco_nex, cidade="Santo André"):
        item = {
            "id": len(self.produtos) + 1,
            "vendedor": vendedor,
            "produto": produto,
            "preco_nex": preco_nex,
            "preco_reais": preco_nex * 0.10,
            "cidade": cidade,
            "vendido": False
        }
        self.produtos.append(item)
        print(f"Anunciado: {produto} por {preco_nex} NEX (R$ {item['preco_reais']:.2f}) - {vendedor} em {cidade}")
        return item

    def listar_disponiveis(self):
        disponiveis = [p for p in self.produtos if not p["vendido"]]
        print(f"\n--- MARKETPLACE NEXUS - {len(disponiveis)} produtos ---")
        for p in disponiveis:
            print(f"#{p['id']} {p['produto']} - {p['preco_nex']} NEX - {p['vendedor']} ({p['cidade']})")
        return disponiveis

    def comprar(self, comprador, produto_id, carteira_comprador, carteira_vendedor):
        produto = next((p for p in self.produtos if p["id"] == produto_id), None)
        if not produto:
            return "Produto não encontrado"
        if produto["vendido"]:
            return "Já vendido"
        if carteira_comprador["saldo"] < produto["preco_nex"]:
            return f"Saldo insuficiente. Você tem {carteira_comprador['saldo']} NEX, precisa de {produto['preco_nex']} NEX"

        # Transferência NEX
        carteira_comprador["saldo"] -= produto["preco_nex"]
        carteira_vendedor["saldo"] += produto["preco_nex"]
        produto["vendido"] = True
        produto["comprador"] = comprador
        self.vendas += 1
        self.volume_nex += produto["preco_nex"]

        print(f"VENDA! {comprador} comprou {produto['produto']} de {produto['vendedor']} por {produto['preco_nex']} NEX")
        return f"Compra concluída! Você comprou {produto['produto']}"

# --- TESTE ---
if __name__ == "__main__":
    print("=== MARKETPLACE NEXUS - Teste Fase 3 ===")
    market = MarketplaceNexus()

    # Carteiras simuladas
    matheus = {"nome": "Matheus", "saldo": 1000}
    joao = {"nome": "João - Padaria", "saldo": 100}

    # João anuncia
    market.anunciar("João - Padaria", "Pão de Queijo (6 un)", 15)
    market.anunciar("João - Padaria", "Café + Bolo", 25)
    market.anunciar("Maria - Brechó", "Camiseta Vintage", 80)

    market.listar_disponiveis()

    # Matheus compra
    print(market.comprar("Matheus", 1, matheus, joao))
    print(f"Saldo Matheus: {matheus['saldo']} NEX | Saldo João: {joao['saldo']} NEX")
    print(f"Vendas: {market.vendas} | Volume: {market.volume_nex} NEX")
    print("Marketplace online!")
