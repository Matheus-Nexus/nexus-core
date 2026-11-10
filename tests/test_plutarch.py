from agents.plutarch import Plutarch

def test_plutarch_creation():
    plutarch = Plutarch()
    assert plutarch.name == "PLUTARCH"
    assert plutarch.division == "Financeira"
    assert plutarch.role == "Diretor Financeiro"

def test_plutarch_run():
    plutarch = Plutarch()
    result = plutarch.run("analisar saldo")
    assert result == "PLUTARCH aprovou e coordenou: analisar saldo"
