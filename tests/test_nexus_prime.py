from agents.nexus_prime import NexusPrime

def test_nexus_prime_creation():
    prime = NexusPrime()
    assert prime.name == "NEXUS PRIME"
    assert prime.division == "Direcao"
    assert prime.role == "CEO"

def test_nexus_prime_run():
    prime = NexusPrime()
    result = prime.run("decidir estrategia geral")
    assert result == "NEXUS PRIME decidiu: decidir estrategia geral"
