# Calculator.py
class Calculator:
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

    def perform_calculation(self):
        op = None if self.operator is None else str(self.operator).strip()
        if op is None or op == "":
            return "Operator is required"
        if op == "+":
            return self.a + self.b
        if op == "-":
            return self.a - self.b
        if op == "*":
            return self.a * self.b
        if op == "/":
            if self.b == 0:
                return "Cannot divide by 0."
            return self.a / self.b
        if op == "%":
            if self.b == 0:
                return "Cannot divide by 0."
            return self.a % self.b
        return "Invalid Operator"
