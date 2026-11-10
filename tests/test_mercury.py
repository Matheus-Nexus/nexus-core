from agents.mercury import Mercury

def test_mercury_creation():
    mercury = Mercury()
    assert mercury.name == "MERCURY"
    assert mercury.division == "Financeira"
    assert mercury.role == "Executor"

def test_mercury_run():
    mercury = Mercury()
    result = mercury.run("executar pagamento")
    assert result == "MERCURY executou: executar pagamento"
