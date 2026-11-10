from agents.mercury import Mercury

def test_mercury_creation():
    mercury = Mercury()
    assert mercury.name == "MERCURY"
    assert mercury.division == "Operacao"
    assert mercury.role == "Executor"

def test_mercury_run_simples():
    mercury = Mercury()
    result = mercury.run("executar pagamento")
    assert result == "MERCURY executou: executar pagamento"

def test_mercury_pagamento_real():
    mercury = Mercury()
    result = mercury.run("executar pagamento valor 1000 taxa 2")
    assert result == "MERCURY executou pagamento: 1020.00 (valor 1000.0 + taxa 2.0%)"
