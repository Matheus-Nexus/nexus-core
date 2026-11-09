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
def test_get_balance():
    bank = NexusBank()
    bank.deposit(100)
    bank.withdraw(30)
    assert bank.get_balance() == 70
def test_get_balance_does_not_change_balance():
    bank = NexusBank()
    bank.deposit(100)
    bank.get_balance()
    bank.get_balance()
    assert bank.get_balance() == 100
