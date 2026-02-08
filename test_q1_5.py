from question1 import BankAccount

def test_negative_deposit_not_allowed():
    acc = BankAccount("Ravi", 500)
    acc.deposit(-200)
    assert acc.get_balance() == 500