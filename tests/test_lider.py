from agents.lider import Lider

def test_lider_creation():
    lider = Lider()
    assert lider.name == "LIDER"
    assert lider.division == "Engenharia"
    assert lider.role == "Construtor"

def test_lider_run():
    lider = Lider()
    result = lider.run("criar funcao de login")
    assert 'def login(usuario, senha):' in result
    assert 'LIDER criou funcao login' in result

def test_lider_run_simples():
    lider = Lider()
    result = lider.run("criar outra coisa")
    assert result == "LIDER construiu: criar outra coisa"
