from question1 import BankAccount

def test_withdraw_updates_balance():
    acc = BankAccount("John", 1000)
    acc.withdraw(300)
    assert acc.get_balance() == 700
