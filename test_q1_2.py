from question1 import BankAccount

def test_deposit_updates_balance():
    acc = BankAccount("John", 1000)
    acc.deposit(500)
    assert acc.get_balance() == 1500
