from core import NexusCore

def main():
    core = NexusCore()
    tarefas = [
        "decidir estrategia geral",
        "calcular ROI investimento 1000 retorno 1500",
        "calcular ROI investimento 2000 retorno 2600",
        "executar pagamento",
        "analisar saldo",
        "corrigir bug no codigo",
        "criar funcao de login",
        "prever preco do token",
    ]
    print("=== NEXUS CORE INICIADO ===")
    for tarefa in tarefas:
        resultado = core.run(tarefa)
        print(f"> {tarefa} -> {resultado}")
    print("=== FIM ===")

if __name__ == "__main__":
    main()
