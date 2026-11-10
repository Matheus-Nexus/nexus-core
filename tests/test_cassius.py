from agents.cassius import Cassius

def test_cassius_creation():
    cassius = Cassius()
    assert cassius.name == "CASSIUS"
    assert cassius.division == "Financeira"
    assert cassius.role == "Analista"

def test_cassius_run():
    cassius = Cassius()
    result = cassius.run("calcular ROI")
    assert result == "CASSIUS calculou: calcular ROI"
