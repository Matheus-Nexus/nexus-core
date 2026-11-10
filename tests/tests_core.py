from core import NexusCore

def test_core_routes_finance_to_plutarch():
    core = NexusCore()
    result = core.run("analisar saldo")
    assert result == "PLUTARCH aprovou e coordenou: analisar saldo"

def test_core_routes_operations():
    core = NexusCore()
    result = core.run("corrigir bug no codigo")
    assert result == "CORE roteou 'corrigir bug no codigo' para Operacoes - HERMES - agente ainda nao criado"
