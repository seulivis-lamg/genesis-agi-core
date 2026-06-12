class MemoryEngine:
    def __init__(self):
        self.memories = []

    def save_memory(self, memory):
        self.memories.append(memory)

    def get_memories(self):
        return self.memories

    def search(self, keyword):
        return [
            m for m in self.memories
            if keyword.lower() in m.lower()
        ]
