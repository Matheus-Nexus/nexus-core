from agents.oraculo import Oraculo

def test_oraculo_creation():
    oraculo = Oraculo()
    assert oraculo.name == "ORACULO"
    assert oraculo.division == "Inteligencia"
    assert oraculo.role == "Estrategista"

def test_oraculo_run_simples():
    oraculo = Oraculo()
    result = oraculo.run("prever preco do token")
    assert result == "ORACULO previu: prever preco do token"

def test_oraculo_previsao_real():
    oraculo = Oraculo()
    result = oraculo.run("prever preco token atual 2.0 crescimento 10")
    assert result == "ORACULO previu preco futuro: 2.20 (atual 2.0 + 10.0%)"
