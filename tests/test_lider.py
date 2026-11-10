from agents.lider import Lider

def test_lider_creation():
    lider = Lider()
    assert lider.name == "LIDER"
    assert lider.division == "Operacoes"
    assert lider.role == "Engenheiro-Chefe"

def test_lider_run():
    lider = Lider()
    result = lider.run("criar funcao de login")
    assert result == "LIDER construiu: criar funcao de login"
