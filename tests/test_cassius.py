from agents.cassius import Cassius

def test_cassius_creation():
    cassius = Cassius()
    assert cassius.name == "CASSIUS"
    assert cassius.division == "Financeira"
    assert cassius.role == "Analista Financeiro"

def test_cassius_run_simples():
    cassius = Cassius()
    result = cassius.run("calcular ROI")
    assert result == "CASSIUS calculou: calcular ROI"

def test_cassius_roi_real():
    cassius = Cassius()
    result = cassius.run("calcular ROI investimento 1000 retorno 1500")
    assert result == "CASSIUS calculou ROI: 50.0% (investimento 1000.0 -> retorno 1500.0)"
