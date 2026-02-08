"""
Question 2: Combine Lengths of Two Ropes Using and printing the object value (20 Marks)

Problem Description:
A rope has a certain length (in meters).
If two ropes are tied together, the total length becomes the sum of their individual lengths.
In this problem, you will create a class that represents a rope and overload the + operator so that 
two rope objects can be added together.
Also, when you print the object, you should get the length printed

Create a class named Rope with the following requirements:
Instance Variable:
- length (int or float, in meters)

Methods:
1. Initializes the rope length.
2. Method that adds the lengths of two Rope objects
3. Method that returns the length when the object is printed

Returns a new Rope object
If other is not a Rope, return NotImplemented

Example:
rope1 = Rope(5)
rope2 = Rope(7)

print(rope1)
Output:
5

total = rope1 + rope2
print(total)

Output:
12

Constraints:
- Length must be positive
- Both objects should of Rope class
- Do not print inside class methods

Evaluation Rubric (20 Marks):
- Correct length calculation -> 8 marks
- Printing the object value -> 7 marks
- Code logic and readability -> 5 marks
"""

class Rope:
    pass
