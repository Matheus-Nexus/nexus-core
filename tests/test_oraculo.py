from agents.oraculo import Oraculo

def test_oraculo_creation():
    oraculo = Oraculo()
    assert oraculo.name == "ORACULO"
    assert oraculo.division == "Inteligencia"
    assert oraculo.role == "Analista de Dados"

def test_oraculo_run():
    oraculo = Oraculo()
    result = oraculo.run("prever preco do token")
    assert result == "ORACULO previu: prever preco do token"
