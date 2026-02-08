"""
Question 3: Vehicle Type System Using Inheritance (15 Marks)

Problem Description:
You are required to model different types of vehicles using inheritance in Python.

Create the following class structure:
Base Class: Vehicle
Method: get_fuel_type() -> returns string "Unknown"

Child Classes:
1. Car
Overrides get_fuel_type() and returns "Petrol"

2. ElectricCar
Overrides get_fuel_type() and returns "Electric"


Example Usage:
v1 = Car()
v2 = ElectricCar()

print(v1.get_fuel_type())
print(v2.get_fuel_type())

Output:
Petrol
Electric


Constraints:
- Use inheritance correctly
- Method overriding is mandatory
- Do not hardcode values outside methods
- Follow proper class naming conventions

Evaluation Rubric (15 Marks):
- Correct inheritance structure -> 4 marks
- Method overriding -> 6 marks
- Code logic and readability -> 5 marks


"""

class Vehicle:
    pass