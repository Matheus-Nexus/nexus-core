from src.nexus.bank import NexusBank
from src.nexus.exceptions import BankError

def test_deposit():
    bank = NexusBank()
    assert bank.deposit(100) == 100

def test_withdraw_insufficient():
    bank = NexusBank()
    try:
        bank.withdraw(10)
        assert False
    except BankError:
        assert True
