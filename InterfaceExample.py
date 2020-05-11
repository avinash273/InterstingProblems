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
