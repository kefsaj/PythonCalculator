from Calculator.subtraction import subtraction
from Calculator.addition import addition
from Calculator.multiply import multiply
from Calculator.division import division
from Calculator.square import square
from Calculator.squareroot import squareroot

#Python program


# add function

def addition(n1, n2):
    return n1 + n2

# Subract function

def subtraction(n1, n2):
    return n1 - n2

# Multi Function

def multiply(n1, n2):
    return n1 * n2

# divide function

def division(a, b):
    a = float(a)
    b = float(b)
    return round((b/ a), 9)

# square function

def square(a):
    a = float(a)
    return a**2

# squareroot function

def squareroot(a):
    a = float(a)
    return round((a**.5), 4)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = addition(a,b)
        return addition(a,b);

    def subtraction(self, a, b):
        self.result = subtraction(a,b)
        return subtract(a,b);

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

