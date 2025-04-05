# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)  # Output: 15
print("Subtraction:", a - b)  # Output: 5
print("Multiplication:", a * b)  # Output: 50
print("Division:", a / b)  # Output: 2.0
print("Modulus:", a % b)  # used to get the remainder, Output: 0
print("Exponentiation:", a ** b)  # used to raise a to the power of b, Output: 100000
print("Floor Division:", a // b)  # used to get the quotient without the decimal part, Output: 2

# Comparison Operators
print("Equal to:", a == b)  # Output: False
print("Not equal to:", a != b)  # Output: True
print("Greater than:", a > b)  # Output: True
print("Less than:", a < b)  # Output: False
print("Greater than or equal to:", a >= b)  # Output: True
print("Less than or equal to:", a <= b)  # Output: False

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)  # Output: False
print("Logical OR:", x or y)  # Output: True
print("Logical NOT:", not x)  # Output: False

# Bitwise Operators
a = 6  # 110 in binary
b = 3  # 011 in binary
print("Bitwise AND:", a & b)  # Output: 2
print("Bitwise OR:", a | b)  # Output: 7
print("Bitwise XOR:", a ^ b)  # Output: 5
print("Bitwise NOT:", ~a)  # Output: -7
print("Bitwise left shift:", a << 1)  # Output: 12
print("Bitwise right shift:", a >> 1)  # Output: 3

# Assignment Operators
a = 10
a += 5
print("Add and assign:", a)  # Output: 15
a -= 3
print("Subtract and assign:", a)  # Output: 12
a *= 2
print("Multiply and assign:", a)  # Output: 24
a /= 4
print("Divide and assign:", a)  # Output: 6.0

# Membership Operators
lst = [1, 2, 3]
print("2 in list:", 2 in lst)  # Output: True
print("4 not in list:", 4 not in lst)  # Output: True

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)  # Output: True
print("x is not z:", x is not z)  # Output: True

# Other Operators
d = {"key": "value"}
print("Dictionary access:", d["key"])  # Output: value

class MyClass:
    def greet(self):
        return "Hello"

obj = MyClass()
print("Method call:", obj.greet())  # Output: Hello

lst = [10, 20, 30]
print("Indexing:", lst[1])  # Output: 20

def add(a, b):
    return a + b

print("Function call:", add(5, 10))  # Output: 15
