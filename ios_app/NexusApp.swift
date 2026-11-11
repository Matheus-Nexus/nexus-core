// NEXUS App - iOS v1.0 - FASE 3
// Nó Gênesis #001 - Matheus - Santo André, SP

import SwiftUI

struct NexusApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @State private var saldoNEX: Double = 1000
    @State private var saldoReais: Double = 100.00
    @State private var minerando: Bool = false

    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                Text("🔷 NEXUS")
                    .font(.largeTitle)
                    .bold()
                Text("O dinheiro que nasce do seu celular")
                    .font(.subheadline)
                    .foregroundColor(.gray)

                VStack {
                    Text("\(Int(saldoNEX)) NEX")
                        .font(.system(size: 48, weight: .bold))
                    Text("= R$ \(String(format: "%.2f", saldoReais))")
                        .font(.title2)
                        .foregroundColor(.green)
                }
                .padding()
                .background(Color(.systemGray6))
                .cornerRadius(20)

                Button(action: {
                    minerando.toggle()
                    if minerando {
                        saldoNEX += 10
                        saldoReais = saldoNEX * 0.10
                    }
                }) {
                    Text(minerando ? "⛏️ Minerando..." : "⛏️ Começar a Minerar")
                        .font(.headline)
                        .foregroundColor(.white)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(minerando ? Color.orange : Color.blue)
                        .cornerRadius(15)
                }

                HStack(spacing: 15) {
                    ActionButton(titulo: "💸 Pagar", cor: .green)
                    ActionButton(titulo: "📷 QR Code", cor: .purple)
                    ActionButton(titulo: "🛒 Market", cor: .orange)
                }

                Spacer()
                Text("Nó Gênesis #001 - Santo André, SP")
                    .font(.caption)
                    .foregroundColor(.gray)
            }
            .padding()
            .navigationTitle("Minha Carteira")
        }
    }
}

struct ActionButton: View {
    var titulo: String
    var cor: Color
    var body: some View {
        Text(titulo)
            .padding()
            .background(cor.opacity(0.15))
            .cornerRadius(12)
    }
}
