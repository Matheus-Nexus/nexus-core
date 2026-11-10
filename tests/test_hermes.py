from agents.hermes import Hermes

def test_hermes_creation():
    hermes = Hermes()
    assert hermes.name == "HERMES"
    assert hermes.division == "Comunicacao"
    assert hermes.role == "Mensageiro"

def test_hermes_run():
    hermes = Hermes()
    result = hermes.run("corrigir bug no codigo")
    assert result == "HERMES coordenou operacao: corrigir bug no codigo"

def test_hermes_contar_palavras():
    hermes = Hermes()
    result = hermes.run("contar palavras ola mundo nexus")
    assert result == "HERMES contou 3 palavras: ola mundo nexus"
