class Calculator:
    def __init__(self, history):
        self.history = history

    def sum(self, a, b):
        result = a + b
        self.history.store(a, b, result)
        return result