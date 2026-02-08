from question1 import BankAccount

def test_withdraw_more_than_balance_not_allowed():
    acc = BankAccount("John", 500)
    acc.withdraw(800)
    assert acc.get_balance() == 500
