

#Python program


# add function

def Addition(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return n1 + n2

# Subtraction function

def Subtraction(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return n2 - n1

# Multi Function

def Multiply(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return n1 * n2

# divide function

def Division(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    return round((n2/ n1), 9)

# square function

def square(n1):
    n1 = float(n1)
    return n1**2

# squareroot function

def squareroot(n1):
    n1 = float(n1)
    return round((n1**.5), 9 )

class Calculator:
    result = 0

    def __init__(self):
        pass

    def Addition(self, a, b):
        self.result = Addition(a,b)
        return Addition(a,b);

    def Subtraction(self, a, b):
        self.result = Subtraction(a,b)
        return Subtraction(a,b);

    def Multiply(self, a, b):
        self.result = Multiply(a, b)
        return self.result

    def Division(self, a, b):
        self.result = Division(a, b)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result


