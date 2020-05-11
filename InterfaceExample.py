"""
Abstract class implementation
"""

class AdvArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvArithmetic):
    def divisorSum(self, n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += i
        return total


my_calculator = Calculator()
print(my_calculator.divisorSum(6))

"""
Trying inheritance and others
"""

class A:
    static_variable = 0
    def __init__(self):
        print("Init A")

    def feature1(self):
        print("Feature1")

class B:
    def feature3(self):
        print("Feature3")

class C(A, B):
    def feature5(self):
        print("Feature5")

a1 = A()
c1 = C()
