from core import NexusCore

def main():
    core = NexusCore()
    tarefas = [
        "decidir estrategia geral",
        "calcular ROI investimento 1000 retorno 1500",
        "calcular ROI investimento 2000 retorno 2600",
        "executar pagamento valor 1000 taxa 2",
        "analisar saldo",
        "contar palavras ola mundo nexus",
        "criar funcao de login",
        "prever preco token atual 2.0 crescimento 10",
    ]
    print("=== NEXUS CORE INICIADO ===")
    for tarefa in tarefas:
        resultado = core.run(tarefa)
        print(f"> {tarefa} -> {resultado}")
    print("=== FIM ===")

if __name__ == "__main__":
    main()
