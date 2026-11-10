from agents.hermes import Hermes

def test_hermes_creation():
    hermes = Hermes()
    assert hermes.name == "HERMES"
    assert hermes.division == "Operacoes"
    assert hermes.role == "Diretor de Operacoes"

def test_hermes_run():
    hermes = Hermes()
    result = hermes.run("corrigir bug no codigo")
    assert result == "HERMES coordenou operacao: corrigir bug no codigo"
