from question1 import BankAccount

def test_negative_withdraw_not_allowed():
    acc = BankAccount("Ravi", 500)
    acc.withdraw(-100)
    assert acc.get_balance() == 500
