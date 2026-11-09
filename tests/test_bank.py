import pytest
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
def test_transfer():
    bank_a = NexusBank()
    bank_b = NexusBank()
    bank_a.deposit(100)
    bank_a.transfer(30, bank_b)
    assert bank_a.get_balance() == 70
    assert bank_b.get_balance() == 30
def test_transfer_insufficient_funds():
    bank_a = NexusBank()
    bank_b = NexusBank()
    bank_a.deposit(100)
    with pytest.raises(BankError):
        bank_a.transfer(200, bank_b)
    assert bank_a.get_balance() == 100
    assert bank_b.get_balance() == 0
def test_transfer_negative_amount():
    bank_a = NexusBank()
    bank_b = NexusBank()
    bank_a.deposit(100)
    with pytest.raises(BankError):
        bank_a.transfer(-50, bank_b)
    assert bank_a.get_balance() == 100
    assert bank_b.get_balance() == 0
