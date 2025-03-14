class History:
    def __init__(self):
        self.data = []

    def store(self, a, b, result):
        self.data.append((a, b, result))
