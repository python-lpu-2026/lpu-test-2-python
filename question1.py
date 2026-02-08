"""
Question 1: Design a Bank Account Class (20 Marks)

Problem Description:
Create a Python class that represents a simple bank account. 
The class should support depositing and withdrawing money while maintaining the account balance.

Create a class named BankAccount with the following requirements:
Instance Variables:
account_holder (string)
balance (integer or float)

Methods:
deposit(amount) -> adds amount to balance
withdraw(amount) -> subtracts amount if sufficient balance exists
get_balance() -> returns current balance

Withdrawal should not be allowed if amount is greater than available balance.


Example Usage:
acc = BankAccount("John", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())

Output:
1200

Constraints:
- Balance should never become negative
- Do not print inside methods (return values only)
- Amount must be positive
- Negative deposit should not be allowed
- Negative withdrawal should not be allowed

Evaluation Rubric (20 Marks):
Correct class & constructor -> 3 marks
Instance variable usage -> 2 marks
Deposit & withdraw -> 8 marks
Code logic and readability -> 7 marks

Implement the below class - BankAccount

"""

class BankAccount:
    pass