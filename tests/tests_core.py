from core import NexusCore

def test_core_routes_finance():
    core = NexusCore()
    result = core.run("analisar saldo")
    assert result == "CORE roteou 'analisar saldo' para Financeira - PLUTARCH"

def test_core_routes_operations():
    core = NexusCore()
    result = core.run("corrigir bug no codigo")
    assert result == "CORE roteou 'corrigir bug no codigo' para Operacoes - HERMES"
