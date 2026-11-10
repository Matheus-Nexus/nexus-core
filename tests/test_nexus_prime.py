from agents.nexus_prime import NexusPrime

def test_nexus_prime_creation():
    prime = NexusPrime()
    assert prime.name == "NEXUS PRIME"
    assert prime.division == "Estrategia"
    assert prime.role == "Decisor"

def test_nexus_prime_aprova_roi_alto():
    prime = NexusPrime()
    prime.memoria["limite_roi"] = 30.0
    result = prime.run("decidir estrategia ROI investimento 1000 retorno 1500")
    assert "APROVOU" in result
    assert "50.0%" in result

def test_nexus_prime_rejeita_roi_baixo():
    prime = NexusPrime()
    prime.memoria["limite_roi"] = 30.0
    result = prime.run("decidir estrategia ROI investimento 1000 retorno 1100")
    assert "REJEITOU" in result

def test_nexus_prime_aprende_erro():
    prime = NexusPrime()
    result = prime.run("erro sistema caiu")
    assert "aprendeu com erro" in result.lower()
