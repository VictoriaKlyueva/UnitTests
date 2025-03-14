class Calculator:
    def __init__(self, history):
        self.history = history

    def sum(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба значения должны быть числами")
        result = a + b
        self.history.store(a, b, result)
        return result