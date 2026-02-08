from question1 import BankAccount

def test_initial_balance():
    acc = BankAccount("John", 1000)
    assert acc.get_balance() == 1000

