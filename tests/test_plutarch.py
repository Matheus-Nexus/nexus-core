from agents.plutarch import Plutarch

def test_plutarch_creation():
    plutarch = Plutarch()
    assert plutarch.name == "PLUTARCH"
    assert plutarch.division == "Financeira"
    assert plutarch.role == "Aprovador"

def test_plutarch_run():
    plutarch = Plutarch()
    result = plutarch.run("analisar saldo")
    assert result == "PLUTARCH aprovou e coordenou: analisar saldo"

def test_plutarch_saldo_real():
    plutarch = Plutarch()
    result = plutarch.run("analisar saldo inicial 5000 gasto 1200")
    assert result == "PLUTARCH analisou saldo: 3800.00 (inicial 5000.0 - gasto 1200.0)"
