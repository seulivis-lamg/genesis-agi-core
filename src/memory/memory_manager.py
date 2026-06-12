class MemoryManager:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def remember(self, data):
        self.short_term.append(data)

    def consolidate(self):
        self.long_term.extend(self.short_term)
        self.short_term.clear()

    def recall(self):
        return self.long_term
